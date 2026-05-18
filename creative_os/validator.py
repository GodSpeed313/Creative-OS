"""Creative OS v0.1 — .cos validator. Parses and produces an IR dict."""

from pathlib import Path
from lark import Transformer, Tree

from creative_os.parser import parse_file

TENSION_ORDER = ["low", "elevated", "medium", "high", "heavy", "extreme"]


class _IRTransformer(Transformer):

    def start(self, items):
        ir = {
            "domain":      {},
            "north_star":  {},
            "entities":    {},
            "constraints": [],
            "enforce":     {},
        }
        for item in items:
            if not isinstance(item, dict):
                continue
            for k, v in item.items():
                if k == "constraints" and isinstance(v, list):
                    ir["constraints"].extend(v)
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


def _merge_ir(raw: dict) -> dict:
    """Merge multi-declaration IR into a single flat structure."""
    ir = {"domain": {}, "north_star": {}, "entities": {}, "constraints": [], "enforce": {}}
    for key, val in raw.items():
        if key == "constraints":
            if isinstance(val, list):
                ir["constraints"].extend(val)
        elif key == "entities":
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
    if not ir["north_star"].get("thesis"):
        errors.append("north_star: missing thesis")
    if not ir["north_star"].get("tension_curve"):
        errors.append("north_star: missing tension_curve")
    if not ir["constraints"]:
        errors.append("enforce: no constraints defined")
    return errors
