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
