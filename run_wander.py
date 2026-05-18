"""run_wander.py — Run the Wander Engine against a draft snapshot.

Usage:
    python run_wander.py
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
    ir       = _load(M1 / "ir.json")
    snapshot = _load(M1 / "draft_snapshot.json")

    from creative_os.engine import evaluate
    trace, rendered, exit_code = evaluate(ir, snapshot)

    print(rendered)

    if exit_code == 1:
        ts   = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
        dest = M1 / "alerts" / f"{ts}.txt"
        dest.write_text(rendered, encoding="utf-8")
        print(f"\nAlert saved -> {dest}")
    else:
        print("\nNo drift detected — alert not saved.")


if __name__ == "__main__":
    main()
