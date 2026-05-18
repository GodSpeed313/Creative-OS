"""Creative OS v0.1 — .cos file parser."""

import sys
from pathlib import Path
from lark import Lark, UnexpectedCharacters, UnexpectedToken, UnexpectedEOF

GRAMMAR_PATH = Path(__file__).parent / "creative_os.lark"

_parser: Lark | None = None


def build_parser() -> Lark:
    global _parser
    if _parser is None:
        grammar = GRAMMAR_PATH.read_text(encoding="utf-8")
        _parser = Lark(grammar, parser="earley", propagate_positions=True)
    return _parser


def parse_file(path: str | Path) -> tuple:
    path = Path(path)
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as e:
        return None, f"Cannot read {path}: {e}"

    parser = build_parser()
    try:
        tree = parser.parse(source)
        return tree, None
    except UnexpectedCharacters as e:
        return None, _fmt_error("Unexpected character", str(e), path)
    except UnexpectedEOF as e:
        return None, _fmt_error("Unexpected end of file", str(e), path)
    except UnexpectedToken as e:
        return None, _fmt_error("Unexpected token", str(e), path)


def _fmt_error(kind: str, detail: str, path) -> str:
    return f"{kind} in {path}:\n  {detail}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <file.cos>", file=sys.stderr)
        sys.exit(1)
    tree, error = parse_file(sys.argv[1])
    if error:
        print(error, file=sys.stderr)
        sys.exit(1)
    print(tree.pretty())
    print(f"\nOK  {sys.argv[1]}")
