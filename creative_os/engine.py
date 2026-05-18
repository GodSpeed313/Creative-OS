"""Creative OS v0.1 — Wander Engine. Evaluates a draft snapshot against a North Star IR."""

from __future__ import annotations

TENSION_ORDER = ["low", "elevated", "medium", "high", "heavy", "extreme"]


def _tension_index(level: str) -> int:
    try:
        return TENSION_ORDER.index(level.lower())
    except ValueError:
        return -1


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
    entities   = ir["entities"]
    enforce    = ir.get("enforce", {})

    active_constraints = enforce.get("constraints", [])
    constraint_map     = {c["name"]: c for c in ir["constraints"]}

    results = []

    for cname in active_constraints:
        constraint = constraint_map.get(cname)
        if not constraint:
            continue

        rule     = constraint.get("rule", {})
        weight   = constraint.get("weight", "core")
        on_drift = constraint.get("on_drift", "flag + alert")
        kind     = rule.get("kind") if isinstance(rule, dict) else None

        status  = "satisfied"
        detail  = ""
        finding = ""

        if kind == "tension_floor":
            floor_level   = north_star.get("tension_curve", {}).get("floor", "medium")
            current_level = scene.get("tension_level", "")
            if current_level and _tension_index(current_level) < _tension_index(floor_level):
                status  = "drift"
                detail  = f"tension_level is '{current_level}', floor is '{floor_level}'"
                finding = f"Kinetic Deviation — tension dropped below declared floor"
            else:
                detail = f"tension_level = '{current_level}', meets floor '{floor_level}'"

        elif kind == "match":
            target_name = constraint.get("target", "")
            entity      = entities.get(target_name, {})
            char_actions = scene.get("character_actions", [])
            for action in char_actions:
                if action.get("character") == target_name:
                    if action.get("physics_match") is False:
                        status  = "drift"
                        detail  = f"{target_name}: action '{action.get('action', '')}' violates declared physics"
                        finding = f"Physics Violation — {target_name} acting outside declared logic"
                        break
            if status == "satisfied":
                detail = f"{target_name}: behavior consistent with declared physics"

        elif kind == "balance":
            lore_ratio = scene.get("lore_expansion_ratio", 0.0)
            if lore_ratio > 0.5:
                status  = "drift"
                detail  = f"lore_expansion_ratio = {lore_ratio} — exceeds 0.5 threshold"
                finding = f"Lore Creep detected — world-building volume overwhelming core plot signal"
            else:
                detail = f"lore_expansion_ratio = {lore_ratio} — within bounds"

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
