"""Creative OS M2 — Wander Engine. Evaluates a draft snapshot against a North Star IR."""

from __future__ import annotations

# M2 alias constants — named levels map to float values per spec
TENSION_ALIASES: dict[str, float] = {
    "low":      0.10,
    "elevated": 0.25,
    "medium":   0.37,
    "high":     0.50,
    "heavy":    0.75,
    "extreme":  1.00,
}

KINETIC_VARIANCE_THRESHOLD = 0.05


def _tension_float(value) -> float | None:
    """Resolve a named alias or float string to a float. Returns None if unresolvable."""
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).lower().strip()
    if s in TENSION_ALIASES:
        return TENSION_ALIASES[s]
    try:
        return float(s)
    except ValueError:
        return None


def _check_tension_floor(north_star: dict, scene: dict) -> tuple[str, str, str]:
    status, detail, finding = "satisfied", "", ""
    current_raw   = scene.get("tension_level", "")
    intent_params = north_star.get("intent_parameters", {})

    if "tension_baseline" in intent_params:
        # M2: float variance check against declared baseline
        baseline_val = _tension_float(intent_params["tension_baseline"])
        current_val  = _tension_float(current_raw) if current_raw else None
        if current_val is not None and baseline_val is not None:
            variance = abs(current_val - baseline_val)
            if variance > KINETIC_VARIANCE_THRESHOLD:
                status  = "drift"
                detail  = (
                    f"tension={current_val:.2f}, baseline={baseline_val:.2f},"
                    f" Δ={variance:.2f}"
                )
                finding = (
                    f"WANDER_ALARM_KINETIC_DEVIATION — variance {variance:.2f}"
                    f" exceeds ±{KINETIC_VARIANCE_THRESHOLD} threshold"
                )
            else:
                detail = (
                    f"tension={current_val:.2f}, baseline={baseline_val:.2f},"
                    f" Δ={variance:.2f} — within threshold"
                )
        else:
            detail = f"tension_level='{current_raw}' — unresolvable"
    else:
        # M1 compat: simple floor check using alias mapping
        floor_raw   = north_star.get("tension_curve", {}).get("floor", "medium")
        floor_val   = _tension_float(floor_raw)
        current_val = _tension_float(current_raw) if current_raw else None
        if current_val is not None and floor_val is not None:
            if current_val < floor_val:
                status  = "drift"
                detail  = (
                    f"tension='{current_raw}' ({current_val:.2f}),"
                    f" floor='{floor_raw}' ({floor_val:.2f})"
                )
                finding = "WANDER_ALARM_KINETIC_DEVIATION — tension dropped below declared floor"
            else:
                detail = (
                    f"tension='{current_raw}' ({current_val:.2f}),"
                    f" meets floor '{floor_raw}' ({floor_val:.2f})"
                )
        else:
            detail = f"tension_level='{current_raw}', floor='{floor_raw}'"

    return status, detail, finding


def _check_physics_match(constraint: dict, scene: dict) -> tuple[str, str, str]:
    status, detail, finding = "satisfied", "", ""
    target_name  = constraint.get("target", "")
    char_actions = scene.get("character_actions", [])
    for action in char_actions:
        if action.get("character") == target_name:
            if action.get("physics_match") is False:
                action_text = action.get("action", "")
                status  = "drift"
                detail  = f"{target_name}: action '{action_text}' violates declared physics"
                finding = (
                    f"WANDER_ALARM_PHYSICS_VIOLATION —"
                    f" {target_name} acting outside declared logic"
                )
                break
    if status == "satisfied":
        detail = f"{target_name}: behavior consistent with declared physics"
    return status, detail, finding


def _check_lore_balance(scene: dict) -> tuple[str, str, str]:
    lore_ratio = scene.get("lore_expansion_ratio", 0.0)
    if lore_ratio > 0.5:
        return (
            "drift",
            f"lore_expansion_ratio={lore_ratio} — exceeds 0.5 threshold",
            "WANDER_ALARM_LORE_CREEP — world-building volume overwhelming core plot signal",
        )
    return "satisfied", f"lore_expansion_ratio={lore_ratio} — within bounds", ""


def evaluate(ir: dict, snapshot: dict) -> tuple[dict, str, int]:
    """
    Evaluate a draft snapshot against the compiled IR.
    Returns (trace, rendered_alert, exit_code).
    exit_code 0 = clean, 1 = drift detected.
    """
    scene      = snapshot.get("scene_state", {})
    project    = ir["domain"].get("project", "Unknown Project")
    scene_id   = snapshot.get("scene_id", "unknown")
    north_star = ir["north_star"]
    enforce    = ir.get("enforce", {})

    constraint_map = {c["name"]: c for c in ir["constraints"]}
    results        = []

    for cname in enforce.get("constraints", []):
        constraint = constraint_map.get(cname)
        if not constraint:
            continue

        rule     = constraint.get("rule", {})
        weight   = constraint.get("weight", "core")
        on_drift = constraint.get("on_drift", "flag + alert")
        kind     = rule.get("kind") if isinstance(rule, dict) else None

        if kind == "tension_floor":
            status, detail, finding = _check_tension_floor(north_star, scene)
        elif kind == "match":
            status, detail, finding = _check_physics_match(constraint, scene)
        elif kind == "balance":
            status, detail, finding = _check_lore_balance(scene)
        else:
            status, detail, finding = "satisfied", f"unknown rule kind: {kind}", ""

        results.append({
            "name":     cname,
            "weight":   weight,
            "status":   status,
            "detail":   detail,
            "finding":  finding,
            "on_drift": on_drift,
        })

    drift_results = [r for r in results if r["status"] == "drift"]
    exit_code     = 1 if drift_results else 0
    system_state  = "drifting" if drift_results else "aligned"

    trace = {
        "project":      project,
        "scene_id":     scene_id,
        "system_state": system_state,
        "constraints":  results,
    }

    from creative_os.alert import render_alert
    rendered = render_alert(trace, ir, snapshot)
    return trace, rendered, exit_code
