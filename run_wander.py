"""run_wander.py — Run the Wander Engine against a draft snapshot.

Usage:
    python run_wander.py                              # defaults to m1/
    python run_wander.py <ir.json> <snapshot.json>
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).parent
M1   = ROOT / "m1"


def _load(path: Path) -> dict:
    for enc in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            return json.loads(path.read_bytes().decode(enc))
        except (UnicodeDecodeError, ValueError):
            continue
    print(f"ERROR: cannot decode '{path}'", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    if len(sys.argv) == 3:
        ir_path       = Path(sys.argv[1])
        snapshot_path = Path(sys.argv[2])
        alerts_dir    = snapshot_path.parent / "alerts"
    else:
        ir_path       = M1 / "ir.json"
        snapshot_path = M1 / "draft_snapshot.json"
        alerts_dir    = M1 / "alerts"

    ir       = _load(ir_path)
    snapshot = _load(snapshot_path)

    from creative_os.engine import evaluate
    trace, rendered, exit_code = evaluate(ir, snapshot)

    print(rendered)

    if exit_code == 1:
        alerts_dir.mkdir(parents=True, exist_ok=True)
        ts   = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
        dest = alerts_dir / f"{ts}.txt"
        dest.write_text(rendered, encoding="utf-8")
        print(f"\nAlert saved -> {dest}")
    else:
        print("\nNo drift detected — alert not saved.")


if __name__ == "__main__":
    main()
