from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ShopifyGoodsAllRequest(BaseModel):
    """Shopify 商品搜索请求参数（字段可选，提供提示用）"""

    model_config = ConfigDict(extra="forbid")

    # 基础参数
    page: int | None = Field(None, description="页码，默认 1")
    size: int | None = Field(None, description="每页条数，默认 20")
    orderBy: str | None = Field('created_time', description="排序字段，见文档 7.1")
    orderType: str | None = Field('desc', description="排序方式：desc / asc")
    rank_type: str | None = Field('search', description="排名类型")
    customized: str | None = Field(None, description="私人定制：-1-全部 / 1-定制")

    # 文本搜索参数
    product_name: str | None = Field(
        None, description="商品名称关键词，支持 | 或 & 组合搜索"
    )
    domain: str | None = Field(None, description="店铺域名")

    # 分类筛选
    category_id: str | int | None = Field(None, description="分类 ID")

    # 价格区间
    min_price_start: float | int | None = Field(None, description="最低价格起始值（美元）")
    min_price_end: float | int | None = Field(None, description="最低价格结束值（美元）")

    # 时间筛选
    created_time_start: int | None = Field(None, description="商品创建开始时间戳（秒）")
    created_time_end: int | None = Field(None, description="商品创建结束时间戳（秒）")


class ShopifyGoodsAllResponse(BaseModel):
    """透传响应结构（不做字段约束，仅标注常见字段）"""

    code: int
    message: str
    data: dict[str, Any] | None = None
