"""Creative OS v0.1 — .cos validator. Parses and produces an IR dict."""

from pathlib import Path
from lark import Transformer, Tree

from creative_os.parser import parse_file

TENSION_ORDER = ["low", "elevated", "medium", "high", "heavy", "extreme"]


class _IRTransformer(Transformer):

    def start(self, items):
        ir = {
            "domain":                 {},
            "north_star":             {},
            "entities":               {},
            "constraints":            [],
            "enforce":                {},
            "intentional_deviations": [],
            "sandbox_commits":        [],
        }
        list_keys = {"constraints", "intentional_deviations", "sandbox_commits"}
        for item in items:
            if not isinstance(item, dict):
                continue
            for k, v in item.items():
                if k in list_keys and isinstance(v, list):
                    ir[k].extend(v)
                elif k == "entities" and isinstance(v, dict):
                    ir["entities"].update(v)
                elif isinstance(v, dict):
                    ir[k].update(v)
                else:
                    ir[k] = v
        return ir

    def declaration(self, items):
        return items[0] if items else {}

    # ── Domain ────────────────────────────────────────────────────────────────

    def domain_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"domain": body}

    def domain_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def domain_field(self, items):
        return items[0] if items else {}

    def project_field(self, items):
        return {"project": str(items[0]).strip('"')}

    def standard_field(self, items):
        return {"standard": str(items[0])}

    # ── North Star ────────────────────────────────────────────────────────────

    def north_star_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"north_star": body}

    def north_star_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def north_star_field(self, items):
        return items[0] if items else {}

    def thesis_field(self, items):
        return {"thesis": str(items[0]).strip('"')}

    def tension_curve_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"tension_curve": body}

    def tension_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def tension_field(self, items):
        return items[0] if items else {}

    def baseline_field(self, items):
        return {"baseline": str(items[0])}

    def floor_field(self, items):
        return {"floor": str(items[0])}

    # ── Entity ────────────────────────────────────────────────────────────────

    def entity_decl(self, items):
        name = str(items[0]).strip('"')
        body = {"logic": [], "sync": []}
        for item in items[1:]:
            if isinstance(item, dict):
                for k, v in item.items():
                    if k in ("logic", "sync"):
                        if isinstance(v, list):
                            body[k].extend(v)
                        else:
                            body[k].append(v)
        return {"entities": {name: body}}

    def entity_body(self, items):
        result = {"logic": [], "sync": []}
        for item in items:
            if isinstance(item, dict):
                for k, v in item.items():
                    if k in result:
                        result[k].append(v)
        return result

    def entity_field(self, items):
        return items[0] if items else {}

    def logic_field(self, items):
        return {"logic": str(items[0]).strip('"')}

    def sync_field(self, items):
        return {"sync": str(items[0]).strip('"')}

    # ── Constraints ───────────────────────────────────────────────────────────

    def constraint_decl(self, items):
        name = str(items[0])
        body = {"name": name}
        for item in items[1:]:
            if isinstance(item, dict):
                body.update(item)
        constraints = [body]
        return {"constraints": constraints}

    def constraint_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def constraint_field(self, items):
        return items[0] if items else {}

    def target_field(self, items):
        return {"target": str(items[0]).strip('"')}

    def rule_field(self, items):
        return {"rule": items[0] if items else {}}

    def weight_field(self, items):
        return {"weight": str(items[0])}

    def on_drift_field(self, items):
        return {"on_drift": items[0] if items else "flag"}

    def tension_floor_rule(self, items):
        return {"kind": "tension_floor", "field": str(items[0])}

    def match_rule(self, items):
        return {"kind": "match", "field": str(items[0]), "target": str(items[1])}

    def balance_rule(self, items):
        return {"kind": "balance", "subject": str(items[0]), "object": str(items[1])}

    def drift_action(self, items):
        return " + ".join(str(i) for i in items if str(i) != "+")

    # ── Enforce ───────────────────────────────────────────────────────────────

    def enforce_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"enforce": body}

    def enforce_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def enforce_field(self, items):
        return items[0] if items else {}

    def north_star_active(self, items):
        return {"north_star": "active"}

    def constraints_field(self, items):
        flat = items[0] if items and isinstance(items[0], list) else list(items)
        return {"constraints": [str(i) for i in flat]}

    def constraint_list(self, items):
        return [str(i) for i in items]

    # ── M2 Intent Parameters ──────────────────────────────────────────────────

    def intent_parameters_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"intent_parameters": body}

    def intent_param_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def intent_param_field(self, items):
        return items[0] if items else {}

    def tension_baseline_field(self, items):
        val = str(items[0]).strip()
        try:
            return {"tension_baseline": float(val)}
        except ValueError:
            return {"tension_baseline": val}

    def physics_integrity_field(self, items):
        return {"physics_integrity": str(items[0])}

    def lore_balance_field(self, items):
        return {"lore_balance": str(items[0])}

    def behavioral_sync_field(self, items):
        return {"behavioral_synchronicity": str(items[0])}

    # ── Intentional Deviation Protocol (IDP) ─────────────────────────────────

    def intentional_deviation_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"intentional_deviations": [body]}

    def idp_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def idp_field(self, items):
        return items[0] if items else {}

    def idp_target_field(self, items):
        return {"target": str(items[0])}

    def idp_intent_field(self, items):
        return {"intent": str(items[0]).strip('"')}

    def idp_scope_field(self, items):
        return {"scope": items[0] if items else {}}

    def idp_sync_override_field(self, items):
        return {"sync_override": items[0] if items else []}

    def idp_resolution_field(self, items):
        return {"resolution": items[0] if items else {}}

    def resolution_revert(self, items):
        return {"type": "revert"}

    def resolution_evolve(self, items):
        return {"type": "evolve", "evolved_to": str(items[0]).strip('"')}

    def scope_range(self, items):
        return {"type": "range", "start": str(items[0]), "end": str(items[1])}

    def scope_single(self, items):
        return {"type": "single", "unit": str(items[0])}

    def delta_path_list(self, items):
        return [str(i) for i in items]

    # ── Sandbox Commit ────────────────────────────────────────────────────────

    def sandbox_commit_decl(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"sandbox_commits": [body]}

    def sandbox_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def sandbox_field(self, items):
        return items[0] if items else {}

    def sandbox_source_field(self, items):
        return {"source_sandbox": str(items[0]).strip('"')}

    def source_ref(self, items):
        return str(items[0]).strip('"')

    def sandbox_deltas_field(self, items):
        return {"commit_deltas": items[0] if items else []}

    def sandbox_reanchor_field(self, items):
        body = {}
        for item in items:
            if isinstance(item, dict):
                body.update(item)
        return {"reanchor_north_star": body}

    def sandbox_vibe_field(self, items):
        return {"vibe_check_verification": str(items[0])}

    def reanchor_body(self, items):
        result = {}
        for item in items:
            if isinstance(item, dict):
                result.update(item)
        return result

    def reanchor_field(self, items):
        return items[0] if items else {}

    def reanchor_thesis_field(self, items):
        return {"new_thesis": str(items[0]).strip('"')}

    def reanchor_floor_field(self, items):
        val = str(items[0]).strip()
        try:
            return {"new_tension_floor": float(val)}
        except ValueError:
            return {"new_tension_floor": val}


def _merge_ir(raw: dict) -> dict:
    """Merge multi-declaration IR into a single flat structure."""
    ir = {
        "domain":                 {},
        "north_star":             {},
        "entities":               {},
        "constraints":            [],
        "enforce":                {},
        "intentional_deviations": [],
        "sandbox_commits":        [],
    }
    list_keys = {"constraints", "intentional_deviations", "sandbox_commits"}
    for key, val in raw.items():
        if key in list_keys and isinstance(val, list):
            ir[key].extend(val)
        elif key == "entities" and isinstance(val, dict):
            ir["entities"].update(val)
        elif isinstance(val, dict):
            ir[key].update(val)
    return ir


def validate_file(path: str | Path) -> tuple[bool, list[str], dict]:
    """Parse and validate a .cos file. Returns (ok, errors, ir)."""
    tree, error = parse_file(path)
    if error:
        return False, [error], {}

    try:
        raw = _IRTransformer().transform(tree)
        ir  = _merge_ir(raw)
    except Exception as e:
        return False, [f"IR build failed: {e}"], {}

    errors = _validate_ir(ir)
    return len(errors) == 0, errors, ir


def _validate_ir(ir: dict) -> list[str]:
    errors = []
    ns = ir["north_star"]
    if not ns.get("thesis"):
        errors.append("north_star: missing thesis / original_thesis")
    has_tension = ns.get("tension_curve") or ns.get("intent_parameters", {}).get("tension_baseline") is not None
    if not has_tension:
        errors.append("north_star: missing tension_curve (M1) or intent_parameters.tension_baseline (M2)")
    if not ir["constraints"]:
        errors.append("enforce: no constraints defined")
    return errors
