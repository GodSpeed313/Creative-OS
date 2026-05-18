"""Creative OS v0.1 — VIBE-CONSTRAINT ALERT formatter."""

from __future__ import annotations
from datetime import datetime, timezone


def render_alert(trace: dict, ir: dict, snapshot: dict) -> str:
    project      = trace["project"]
    scene_id     = trace["scene_id"]
    system_state = trace["system_state"]
    thesis       = ir["north_star"].get("thesis", "")
    timestamp    = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    constraints  = trace["constraints"]
    drift_items  = [c for c in constraints if c["status"] == "drift"]

    lines = []
    W = 60

    lines.append("VIBE-CONSTRAINT ALERT" if drift_items else "NARRATIVE ALIGNMENT CHECK")
    lines.append("═" * W)
    lines.append(f"Timestamp    : {timestamp}")
    lines.append(f"Project      : {project}")
    lines.append(f"Scene        : {scene_id}")
    lines.append(f"Thesis       : {thesis[:W - 15]}..." if len(thesis) > W - 15 else f"Thesis       : {thesis}")
    lines.append("═" * W)

    for i, c in enumerate(constraints):
        is_last   = i == len(constraints) - 1
        connector = "└──" if is_last else "├──"
        spacer    = "    " if is_last else "│   "

        status_icon = "✓" if c["status"] == "satisfied" else "✗"
        weight_tag  = f"[weight: {c['weight']}]"

        lines.append(f"{connector} CONSTRAINT: {c['name']} {weight_tag}")
        lines.append(f"{spacer}├── Evaluation : {c['detail']}")

        if c["status"] == "drift":
            lines.append(f"{spacer}├── ✗ DRIFT DETECTED")
            lines.append(f"{spacer}├── Finding    : {c['finding']}")
            lines.append(f"{spacer}└── Action     : {c['on_drift']}")
        else:
            lines.append(f"{spacer}└── {status_icon} ALIGNED — no action")

        if not is_last:
            lines.append("│")

    lines.append("│")
    lines.append("└── RESOLUTION")

    if drift_items:
        lines.append(f"    ├── System state : {system_state.upper()}")
        lines.append(f"    ├── Drift count  : {len(drift_items)} violation(s) detected")
        for d in drift_items:
            lines.append(f"    │   · {d['name']} [{d['weight']}] — {d['finding']}")
        lines.append(f"    └── The Wander Alarm has triggered. Review flagged constraints before continuing.")
    else:
        lines.append(f"    ├── System state : {system_state.upper()}")
        lines.append(f"    └── All constraints satisfied. North Star holding. No drift detected.")

    return "\n".join(lines)
