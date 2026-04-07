from typing import Any

from fastmcp import FastMCP

from .category_data import get_etsy_categories as _get_etsy_categories
from .category_data import get_shopify_categories as _get_shopify_categories
from .etsy_models import EtsyGoodsAllRequest
from .etsy_service import EtsyGoodsAllService
from .shopify_models import ShopifyGoodsAllRequest
from .shopify_service import ShopifyGoodsAllService


mcp = FastMCP(
    "IXSPY ETSY Server",
    tasks=True,
)

etsy_service = EtsyGoodsAllService()
shopify_service = ShopifyGoodsAllService()


@mcp.tool(
    name="ixspy.search_etsy_goods_all",
    description="根据多维度筛选条件搜索 Etsy 商品信息，响应原样透传",
)
async def search_etsy_goods_all(payload: EtsyGoodsAllRequest) -> dict[str, Any]:
    return await etsy_service.search(payload)


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


@mcp.tool(
    name="ixspy.search_shopify_goods_all",
    description="根据多维度筛选条件搜索 Shopify 商品信息，响应原样透传",
)
async def search_shopify_goods_all(payload: ShopifyGoodsAllRequest) -> dict[str, Any]:
    return await shopify_service.search(payload)
