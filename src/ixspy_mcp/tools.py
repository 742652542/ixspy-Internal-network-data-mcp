from typing import Any

from fastmcp import FastMCP

from .etsy_models import EtsyGoodsAllRequest
from .etsy_service import EtsyGoodsAllService


mcp = FastMCP(
    "IXSPY FastMCP Server",
    tasks=True,
)

service = EtsyGoodsAllService()


@mcp.tool(
    name="ixspy.search_etsy_goods_all",
    description="根据多维度筛选条件搜索 Etsy 商品信息，响应原样透传",
)
async def search_etsy_goods_all(payload: EtsyGoodsAllRequest) -> dict[str, Any]:
    return await service.search(payload)
