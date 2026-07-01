from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FacebookAdProductsRequest(BaseModel):
    """Facebook 广告产品列表请求参数。"""

    model_config = ConfigDict(extra="forbid")

    page: int | None = Field(None, description="页码，默认 1")
    size: int | None = Field(None, description="每页条数，默认 20")
    category_id: str | int | None = Field(None, description="分类 ID")
    product_name: str | None = Field(None, description="商品名称关键词")
    source_content: str | None = Field(
        None, description="文案内容关键词，支持 | 或 & 组合搜索"
    )
    domain: str | None = Field(None, description="域名")
    created_time_start: int | None = Field(None, description="开始时间戳，单位秒")
    created_time_end: int | None = Field(None, description="结束时间戳，单位秒")
    orderBy: str | None = Field(None, description="排序字段")
    orderType: str | None = Field(None, description="排序方式")


class FacebookLibraryAdListRequest(BaseModel):
    """Facebook 广告库广告列表请求参数。"""

    model_config = ConfigDict(extra="forbid")

    page: int | None = Field(None, description="页码，默认 1")
    size: int | None = Field(None, description="每页条数，默认 20")
    link: str | None = Field(None, description="站点链接或域名")
    cta_type: str | None = Field(None, description="号召类型")
    is_aaa_eligible: str | None = Field(None, description="区域标记")
    body: str | None = Field(None, description="广告正文关键词")
    ad_type: str | None = Field(None, description="广告类型")
    is_active: str | None = Field(None, description="是否投放中")
    start_date: int | None = Field(None, description="开始时间戳，单位秒")
    end_date: int | None = Field(None, description="结束时间戳，单位秒")
    active_days_start: int | None = Field(None, description="投放天数起始")
    active_days_end: int | None = Field(None, description="投放天数结束")
    collation_count_start: int | None = Field(None, description="广告数起始")
    collation_count_end: int | None = Field(None, description="广告数结束")
    collect_start_date: int | None = Field(None, description="采集开始时间戳，单位秒")
    collect_end_date: int | None = Field(None, description="采集结束时间戳，单位秒")
    orderBy: str | None = Field(None, description="排序字段")
    orderType: str | None = Field(None, description="排序方式")
    collation_id: str | None = Field(None, description="聚合 ID")
    page_id: str | None = Field(None, description="page_id")
    archive_id: str | None = Field(None, description="archive_id")
    product_id: str | None = Field(None, description="按产品 ID 查询")
