from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ShopifyGoodsAllRequest(BaseModel):
    """Shopify 商品搜索请求参数（字段可选，提供提示用）"""

    # 基础参数
    page: int | None = Field(None, description="页码，默认 1")
    size: int | None = Field(None, description="每页条数，默认 20")
    orderBy: str | None = Field(None, description="排序字段，见文档 7.1")
    orderType: str | None = Field(None, description="排序方式：desc / asc")
    rank_type: str | None = Field(None, description="排名类型")
    customized: str | None = Field(None, description="自定义标识")

    # 文本搜索参数
    product_name: str | None = Field(
        None, description="商品名称关键词，支持 | 或 & 组合搜索"
    )
    domain: str | None = Field(None, description="店铺域名")
    shop_id: str | None = Field(None, description="店铺 ID")

    # 分类筛选
    category_id: str | None = Field(None, description="分类 ID")

    # 价格区间
    min_price_start: float | int | None = Field(None, description="最低价格起始值（美元）")
    min_price_end: float | int | None = Field(None, description="最低价格结束值（美元）")

    # 销量指数
    sales_7_count_start: int | None = Field(None, description="7 天销量指数起始值")
    sales_7_count_end: int | None = Field(None, description="7 天销量指数结束值")

    # 时间筛选
    saled_time_start: int | None = Field(None, description="最后销售开始时间戳（秒）")
    saled_time_end: int | None = Field(None, description="最后销售结束时间戳（秒）")
    created_time_start: int | None = Field(None, description="商品创建开始时间戳（秒）")
    created_time_end: int | None = Field(None, description="商品创建结束时间戳（秒）")
    created_time: list[int] | None = Field(None, description="创建时间范围数组")
    update_time_start: int | None = Field(None, description="商品更新开始时间戳（秒）")
    update_time_end: int | None = Field(None, description="商品更新结束时间戳（秒）")


class ShopifyGoodsAllResponse(BaseModel):
    """透传响应结构（不做字段约束，仅标注常见字段）"""

    code: int
    message: str
    data: dict[str, Any] | None = None
