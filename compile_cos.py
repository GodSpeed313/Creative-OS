"""compile_cos.py — Compile a .cos file to ir.json.

Usage:
    python compile_cos.py <file.cos> [output_ir.json]
"""

import json
import sys
from pathlib import Path

from creative_os.validator import validate_file


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python compile_cos.py <file.cos> [output_ir.json]", file=sys.stderr)
        sys.exit(1)

    cos_path = Path(sys.argv[1])
    if not cos_path.exists():
        print(f"ERROR: {cos_path} not found", file=sys.stderr)
        sys.exit(1)

    out_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else cos_path.with_name("ir.json")

    ok, errors, ir = validate_file(str(cos_path))
    if not ok:
        print("Validation errors:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    out_path.write_text(json.dumps(ir, indent=2), encoding="utf-8")
    print(f"OK  {cos_path} -> {out_path}  ({len(ir['constraints'])} constraints, {len(ir['entities'])} entities)")


if __name__ == "__main__":
    main()
