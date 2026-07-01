from typing import Any

from fastmcp import FastMCP

from .category_data import get_etsy_categories as _get_etsy_categories
from .category_data import get_shopify_categories as _get_shopify_categories
from .category_data import search_etsy_categories as _search_etsy_categories
from .category_data import search_shopify_categories as _search_shopify_categories
from .category_models import CategorySearchRequest
from .etsy_models import EtsyGoodsAllRequest
from .etsy_service import EtsyGoodsAllService
from .facebook_models import FacebookAdProductsRequest, FacebookLibraryAdListRequest
from .facebook_service import FacebookService
from .request_logging import log_error, log_request
from .shopify_models import ShopifyGoodsAllRequest
from .shopify_service import ShopifyGoodsAllService


mcp = FastMCP(
    "IXSPY Etsy/Shopify Server",
    tasks=True,
)

etsy_service = EtsyGoodsAllService()
shopify_service = ShopifyGoodsAllService()
facebook_service = FacebookService()


@mcp.tool(
    name="ixspy.search_etsy_goods_all",
    description="根据多维度筛选条件搜索 Etsy 商品信息，响应原样透传",
)
async def search_etsy_goods_all(payload: EtsyGoodsAllRequest) -> dict[str, Any]:
    log_request(tool="ixspy.search_etsy_goods_all", payload=payload)
    try:
        return await etsy_service.search(payload)
    except Exception as exc:  # noqa: BLE001 - re-raise after logging
        log_error(tool="ixspy.search_etsy_goods_all", payload=payload, error=exc)
        raise


@mcp.tool(
    name="ixspy.get_etsy_categories",
    description="获取 Etsy 分类树数据",
)
async def get_etsy_categories() -> dict[str, Any]:
    log_request(tool="ixspy.get_etsy_categories", payload={})
    try:
        return {"code": 0, "message": "", "data": _get_etsy_categories()}
    except RuntimeError as exc:
        log_error(tool="ixspy.get_etsy_categories", payload={}, error=exc)
        return {"code": 1, "message": str(exc), "data": None}


@mcp.tool(
    name="ixspy.get_shopify_categories",
    description="获取 Shopify 分类树数据",
)
async def get_shopify_categories() -> dict[str, Any]:
    log_request(tool="ixspy.get_shopify_categories", payload={})
    try:
        return {"code": 0, "message": "", "data": _get_shopify_categories()}
    except RuntimeError as exc:
        log_error(tool="ixspy.get_shopify_categories", payload={}, error=exc)
        return {"code": 1, "message": str(exc), "data": None}


@mcp.tool(
    name="ixspy.search_etsy_categories",
    description="搜索 Etsy 分类（服务端过滤）",
)
async def search_etsy_categories(payload: CategorySearchRequest) -> dict[str, Any]:
    log_request(tool="ixspy.search_etsy_categories", payload=payload)
    try:
        return {
            "code": 0,
            "message": "",
            "data": _search_etsy_categories(payload.query, payload.limit),
        }
    except RuntimeError as exc:
        log_error(tool="ixspy.search_etsy_categories", payload=payload, error=exc)
        return {"code": 1, "message": str(exc), "data": None}


@mcp.tool(
    name="ixspy.search_shopify_categories",
    description="搜索 Shopify 分类（服务端过滤）",
)
async def search_shopify_categories(payload: CategorySearchRequest) -> dict[str, Any]:
    log_request(tool="ixspy.search_shopify_categories", payload=payload)
    try:
        return {
            "code": 0,
            "message": "",
            "data": _search_shopify_categories(payload.query, payload.limit),
        }
    except RuntimeError as exc:
        log_error(tool="ixspy.search_shopify_categories", payload=payload, error=exc)
        return {"code": 1, "message": str(exc), "data": None}


@mcp.tool(
    name="ixspy.search_shopify_goods_all",
    description="根据多维度筛选条件搜索 Shopify 商品信息，响应原样透传",
)
async def search_shopify_goods_all(payload: ShopifyGoodsAllRequest) -> dict[str, Any]:
    log_request(tool="ixspy.search_shopify_goods_all", payload=payload)
    try:
        return await shopify_service.search(payload)
    except Exception as exc:  # noqa: BLE001 - re-raise after logging
        log_error(tool="ixspy.search_shopify_goods_all", payload=payload, error=exc)
        raise


@mcp.tool(
    name="ixspy.search_facebook_ad_products",
    description="根据分类、关键词、域名和时间范围查询 Facebook 广告产品",
)
async def search_facebook_ad_products(payload: FacebookAdProductsRequest) -> dict[str, Any]:
    log_request(tool="ixspy.search_facebook_ad_products", payload=payload)
    try:
        return await facebook_service.search_ad_products(payload)
    except Exception as exc:  # noqa: BLE001 - re-raise after logging
        log_error(tool="ixspy.search_facebook_ad_products", payload=payload, error=exc)
        raise


@mcp.tool(
    name="ixspy.search_facebook_library_ad_list",
    description="查询 Facebook 广告库广告列表",
)
async def search_facebook_library_ad_list(
    payload: FacebookLibraryAdListRequest,
) -> dict[str, Any]:
    log_request(tool="ixspy.search_facebook_library_ad_list", payload=payload)
    try:
        return await facebook_service.search_library_ad_list(payload)
    except Exception as exc:  # noqa: BLE001 - re-raise after logging
        log_error(
            tool="ixspy.search_facebook_library_ad_list",
            payload=payload,
            error=exc,
        )
        raise
