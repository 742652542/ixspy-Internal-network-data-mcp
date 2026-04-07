# Etsy Goods All Search MCP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a FastMCP tool `ixspy.search_etsy_goods_all` that calls `http://etsy.int.ixspy.com/api/etsy-goods-all` with fully documented parameters and returns the raw JSON response, then remove the `demo/` directory.

**Architecture:** Keep a small service + models + tools layout like the demo. `etsy_models.py` defines a rich request schema for AI hints, `etsy_service.py` handles the HTTP POST and error mapping, `tools.py` registers the MCP tool, and `server.py` runs the MCP server.

**Tech Stack:** Python, FastMCP, Pydantic v2, httpx

---

## File Structure

- Create: `src/ixspy_mcp/__init__.py`
- Create: `src/ixspy_mcp/etsy_models.py`
- Create: `src/ixspy_mcp/etsy_service.py`
- Create: `src/ixspy_mcp/tools.py`
- Create: `server.py`
- Delete: `demo/`

---

### Task 1: Request Models (AI Hints Only)

**Files:**
- Create: `src/ixspy_mcp/__init__.py`
- Create: `src/ixspy_mcp/etsy_models.py`

- [ ] **Step 1: Create `__init__.py`**

```python
"""ixspy_mcp package."""
```

- [ ] **Step 2: Add the request model with full field descriptions**

```python
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class EtsyGoodsAllRequest(BaseModel):
    """Etsy 商品全局搜索请求参数（字段可选，提供提示用）"""

    # 基础参数
    page: str | None = Field(None, description="页码，默认 1")
    size: str | None = Field(None, description="每页条数，默认 20")
    orderBy: str | None = Field(None, description="排序字段，见文档 7.1")
    orderType: str | None = Field(None, description="排序方式：desc / asc")

    # 文本搜索参数
    search_content: str | None = Field(
        None, description="关键词搜索，支持 | 或 &，可输入 URL 或商品 ID"
    )
    search_content_not: str | None = Field(
        None, description="标题过滤词，多词用 | 分隔"
    )
    store_id: str | None = Field(None, description="店铺 ID")
    materials: str | None = Field(None, description="材质搜索")
    categoryIds: list[int] | None = Field(None, description="分类 ID 数组")
    category_path: str | None = Field(None, description="分类路径末级 ID")

    # 标志位筛选（""/不传不限，1 是，-1 否）
    best_seller: int | str | None = Field(None, description="热销标志")
    personalization: int | str | None = Field(None, description="是否支持定制")
    is_ad: int | str | None = Field(None, description="是否为广告商品")
    netfly_tag: int | str | None = Field(None, description="是否已采集")
    etsy_pick: int | str | None = Field(None, description="Etsy's Pick 标记")
    rare_find: int | str | None = Field(None, description="Rare Find 标记")

    # 时间筛选
    day: int | None = Field(None, description="上架时间枚举，0/30/60/90/180/365/366")
    latest_sale_time: int | None = Field(
        None, description="最近卖出时间枚举，含义同 day"
    )
    ad_time_start: str | None = Field(None, description="广告投放开始时间戳（秒）")
    ad_time_end: str | None = Field(None, description="广告投放结束时间戳（秒）")

    # 24 小时内购买人数
    sales_24hours: str | None = Field(None, description="0 / 1-20 / 20+")

    # 数值区间筛选（0 表示不限）
    offer_price_start: float | int | None = Field(None, description="价格起始值（美元）")
    offer_price_end: float | int | None = Field(None, description="价格结束值（美元）")
    max_price_start: float | int | None = Field(None, description="最高价格起始值")
    max_price_end: float | int | None = Field(None, description="最高价格结束值")
    total_price_start: float | int | None = Field(None, description="总价起始值（含运费）")
    total_price_end: float | int | None = Field(None, description="总价结束值（含运费）")
    cost_start: float | int | None = Field(None, description="运费起始值")
    cost_end: float | int | None = Field(None, description="运费结束值")
    favorites_total_start: int | None = Field(None, description="累计收藏数起始值")
    favorites_total_end: int | None = Field(None, description="累计收藏数结束值")
    reviews_total_start: int | None = Field(None, description="累计评论数起始值")
    reviews_total_end: int | None = Field(None, description="累计评论数结束值")
    sales_total_start: int | None = Field(None, description="累计销量起始值")
    sales_total_end: int | None = Field(None, description="累计销量结束值")
    carts_total_start: int | None = Field(None, description="累计加购数起始值")
    carts_total_end: int | None = Field(None, description="累计加购数结束值")
    est_sales_total_start: int | None = Field(None, description="估算总销量起始值")
    est_sales_total_end: int | None = Field(None, description="估算总销量结束值")
    rating_start: float | int | None = Field(None, description="评分起始值（0-5）")
    rating_end: float | int | None = Field(None, description="评分结束值（0-5）")
    process_min: int | None = Field(None, description="预计发货天数最小值")
    process_max: int | None = Field(None, description="预计发货天数最大值")
    received_min: int | None = Field(None, description="预计到货天数最小值")
    received_max: int | None = Field(None, description="预计到货天数最大值")

    # 发货地
    ships_from: list[str] | None = Field(None, description="发货地国家/地区数组")


class EtsyGoodsAllResponse(BaseModel):
    """透传响应结构（不做字段约束，仅标注常见字段）"""

    code: int
    message: str
    data: dict[str, Any] | None = None
```

- [ ] **Step 3: Commit**

```bash
git add src/ixspy_mcp/__init__.py src/ixspy_mcp/etsy_models.py
git commit -m "feat: add etsy goods search request model"
```

---

### Task 2: Service Layer (HTTP Call + Error Handling)

**Files:**
- Create: `src/ixspy_mcp/etsy_service.py`

- [ ] **Step 1: Add the service implementation**

```python
from __future__ import annotations

from typing import Any

import httpx

from .etsy_models import EtsyGoodsAllRequest


class EtsyGoodsAllService:
    def __init__(self, url: str = "http://etsy.int.ixspy.com/api/etsy-goods-all") -> None:
        self._url = url
        self._timeout = httpx.Timeout(30.0)

    async def search(self, payload: EtsyGoodsAllRequest) -> dict[str, Any]:
        data = payload.model_dump(exclude_none=True)
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(self._url, json=data)

        if response.status_code < 200 or response.status_code >= 300:
            snippet = response.text[:200].replace("\n", " ")
            raise RuntimeError(f"HTTP {response.status_code}: {snippet}")

        return response.json()
```

- [ ] **Step 2: Commit**

```bash
git add src/ixspy_mcp/etsy_service.py
git commit -m "feat: add etsy goods search service"
```

---

### Task 3: MCP Tool Registration

**Files:**
- Create: `src/ixspy_mcp/tools.py`

- [ ] **Step 1: Register the MCP tool**

```python
from typing import Any

from fastmcp import FastMCP

from .etsy_models import EtsyGoodsAllRequest
from .etsy_service import EtsyGoodsAllService


mcp = FastMCP(
    "IXSPY ETSY Server",
    tasks=True,
)

service = EtsyGoodsAllService()


@mcp.tool(
    name="ixspy.search_etsy_goods_all",
    description="根据多维度筛选条件搜索 Etsy 商品信息，响应原样透传",
)
async def search_etsy_goods_all(payload: EtsyGoodsAllRequest) -> dict[str, Any]:
    return await service.search(payload)
```

- [ ] **Step 2: Commit**

```bash
git add src/ixspy_mcp/tools.py
git commit -m "feat: add etsy goods search mcp tool"
```

---

### Task 4: Server Entry Point

**Files:**
- Create: `server.py`

- [ ] **Step 1: Add the FastMCP server entry**

```python
from ixspy_mcp.tools import mcp


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)
```

- [ ] **Step 2: Commit**

```bash
git add server.py
git commit -m "feat: add mcp server entry"
```

---

### Task 5: Manual Verification (No Automated Tests)

**Files:**
- No code changes

- [ ] **Step 1: Run the server**

```bash
python server.py
```

- [ ] **Step 2: Call the MCP tool**

```bash
curl -X POST http://localhost:8080/tools/ixspy.search_etsy_goods_all \
  -H "Content-Type: application/json" \
  -d "{\"page\":\"1\",\"size\":\"20\",\"orderBy\":\"favorites_total\",\"orderType\":\"desc\",\"search_content\":\"necklace\"}"
```

Expected: JSON response with `code`, `message`, `data` fields (either success or documented error codes).

- [ ] **Step 3: Commit (optional, no code changes)**

```bash
git status -sb
```

---

### Task 6: Remove Demo Directory

**Files:**
- Delete: `demo/`

- [ ] **Step 1: Delete the demo directory**

```bash
Remove-Item -Recurse -Force "demo"
```

- [ ] **Step 2: Commit**

```bash
git add -A
git commit -m "chore: remove demo directory"
```

---

## Self-Review Checklist

1. **Spec coverage:** All requirements covered: tool name, fixed URL, full field hints, response passthrough, no auth, delete `demo/`.
2. **Placeholder scan:** No TBD/TODO or vague steps.
3. **Type consistency:** `EtsyGoodsAllRequest` referenced consistently in service and tool.
