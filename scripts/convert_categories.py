from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def extract_array(js_text: str) -> list[dict[str, Any]]:
    start = js_text.find("[")
    end = js_text.rfind("]")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("cannot find array literal")
    array_text = js_text[start : end + 1]
    return json.loads(array_text)


def convert(src: Path, dest: Path) -> None:
    data = extract_array(src.read_text(encoding="utf-8"))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=str, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    source_root = Path(args.source_root).resolve() if args.source_root else repo_root
    convert(source_root / "etsy_category.js", repo_root / "src" / "ixspy_mcp" / "data" / "etsy_categories.json")
    convert(source_root / "shopify_category.js", repo_root / "src" / "ixspy_mcp" / "data" / "shopify_categories.json")


if __name__ == "__main__":
    main()
