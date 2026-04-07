# Categories MCP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two MCP tools that return static Etsy/Shopify category trees for category ID lookup.

**Architecture:** Store category trees as JSON files under `src/ixspy_mcp/data/` and load them into module-level caches on startup. Tools return a standard `{code, message, data}` envelope and handle load errors gracefully.

**Tech Stack:** Python, FastMCP, pytest

---

## File Structure

- Create: `scripts/convert_categories.py`
- Create: `src/ixspy_mcp/data/etsy_categories.json`
- Create: `src/ixspy_mcp/data/shopify_categories.json`
- Create: `src/ixspy_mcp/category_data.py`
- Modify: `src/ixspy_mcp/tools.py`
- Modify: `README.md`
- Create: `tests/test_category_data.py`
- Create: `tests/test_tools_categories.py`

---

### Task 1: Generate JSON data files

**Files:**
- Create: `scripts/convert_categories.py`
- Create: `src/ixspy_mcp/data/etsy_categories.json`
- Create: `src/ixspy_mcp/data/shopify_categories.json`

- [ ] **Step 1: Add conversion script**

```python
from __future__ import annotations

import json
from pathlib import Path


def extract_array(js_text: str) -> list[dict]:
    prefix = "var "
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


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    convert(root / "etsy_category.js", root / "src" / "ixspy_mcp" / "data" / "etsy_categories.json")
    convert(root / "shopify_category.js", root / "src" / "ixspy_mcp" / "data" / "shopify_categories.json")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run conversion script to generate JSON**

Run: `python scripts/convert_categories.py`

Expected: Two files created under `src/ixspy_mcp/data/`.

- [ ] **Step 3: Commit**

```bash
git add scripts/convert_categories.py src/ixspy_mcp/data/etsy_categories.json src/ixspy_mcp/data/shopify_categories.json
git commit -m "chore: add category data files"
```

---

### Task 2: Category data loader module

**Files:**
- Create: `src/ixspy_mcp/category_data.py`
- Create: `tests/test_category_data.py`

- [ ] **Step 1: Write failing tests**

```python
from ixspy_mcp.category_data import get_etsy_categories, get_shopify_categories


def test_get_etsy_categories_returns_list():
    data = get_etsy_categories()
    assert isinstance(data, list)
    assert data
    assert "label" in data[0]
    assert "value" in data[0]


def test_get_shopify_categories_returns_list():
    data = get_shopify_categories()
    assert isinstance(data, list)
    assert data
    assert "label" in data[0]
    assert "value" in data[0]
```

- [ ] **Step 2: Run tests to verify failure**

Run: `pytest tests/test_category_data.py -q`

Expected: FAIL with `ModuleNotFoundError: No module named 'ixspy_mcp.category_data'`.

- [ ] **Step 3: Implement category loader**

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _load_categories(filename: str) -> list[dict[str, Any]]:
    data_path = Path(__file__).resolve().parent / "data" / filename
    try:
        raw = data_path.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception as exc:  # noqa: BLE001 - return a concise error upstream
        raise RuntimeError(f"load categories failed: {exc}") from exc


_ETSY_CATEGORIES = _load_categories("etsy_categories.json")
_SHOPIFY_CATEGORIES = _load_categories("shopify_categories.json")


def get_etsy_categories() -> list[dict[str, Any]]:
    return _ETSY_CATEGORIES


def get_shopify_categories() -> list[dict[str, Any]]:
    return _SHOPIFY_CATEGORIES
```

- [ ] **Step 4: Run tests to verify pass**

Run: `pytest tests/test_category_data.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ixspy_mcp/category_data.py tests/test_category_data.py
git commit -m "feat: add category data loader"
```

---

### Task 3: MCP tools for categories

**Files:**
- Modify: `src/ixspy_mcp/tools.py`
- Create: `tests/test_tools_categories.py`

- [ ] **Step 1: Write failing tests**

```python
import asyncio

from ixspy_mcp.tools import get_etsy_categories, get_shopify_categories


def test_get_etsy_categories_tool():
    result = asyncio.run(get_etsy_categories())
    assert result["code"] == 0
    assert isinstance(result["data"], list)


def test_get_shopify_categories_tool():
    result = asyncio.run(get_shopify_categories())
    assert result["code"] == 0
    assert isinstance(result["data"], list)
```

- [ ] **Step 2: Run tests to verify failure**

Run: `pytest tests/test_tools_categories.py -q`

Expected: FAIL with `ImportError` for missing tool functions.

- [ ] **Step 3: Implement MCP tools**

```python
from .category_data import get_etsy_categories as _get_etsy_categories
from .category_data import get_shopify_categories as _get_shopify_categories


@mcp.tool(
    name="ixspy.get_etsy_categories",
    description="获取 Etsy 分类树数据",
)
async def get_etsy_categories() -> dict[str, Any]:
    try:
        return {"code": 0, "message": "", "data": _get_etsy_categories()}
    except RuntimeError as exc:
        return {"code": 1, "message": str(exc), "data": None}


@mcp.tool(
    name="ixspy.get_shopify_categories",
    description="获取 Shopify 分类树数据",
)
async def get_shopify_categories() -> dict[str, Any]:
    try:
        return {"code": 0, "message": "", "data": _get_shopify_categories()}
    except RuntimeError as exc:
        return {"code": 1, "message": str(exc), "data": None}
```

- [ ] **Step 4: Run tests to verify pass**

Run: `pytest tests/test_tools_categories.py -q`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ixspy_mcp/tools.py tests/test_tools_categories.py
git commit -m "feat: add mcp tools for categories"
```

---

### Task 4: Documentation update

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Update README tools list**

```markdown
- MCP 工具：`ixspy.search_etsy_goods_all`
- MCP 工具：`ixspy.search_shopify_goods_all`
- MCP 工具：`ixspy.get_etsy_categories`
- MCP 工具：`ixspy.get_shopify_categories`
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: document category mcp tools"
```

---

## Self-Review Checklist

1. **Spec coverage:** Tools + static JSON data + caching + error handling + docs are covered by Tasks 1-4.
2. **Placeholder scan:** No TBD/TODO/"handle appropriately" statements.
3. **Type consistency:** `get_etsy_categories()` / `get_shopify_categories()` used consistently across tests and tools.
