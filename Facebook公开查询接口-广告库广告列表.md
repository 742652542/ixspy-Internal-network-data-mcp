# Facebook 公开查询接口 - 广告库广告列表

## 一、接口概述

| 项目 | 说明 |
|------|------|
| 接口地址 | `http://etsy.int.ixspy.com/api/facebook/public/library/ad-list` |
| 请求方式 | GET |
| Content-Type | application/json |
| 接口说明 | 查询 Facebook 广告库广告列表 |
| 数据限制 | 支持分页查询 |

---

## 二、请求参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| page | number | 否 | 1 | 页码 |
| size | number | 否 | 20 | 每页条数 |
| link | string | 否 | - | 站点链接或域名 |
| cta_type | string | 否 | - | 号召类型 |
| is_aaa_eligible | string | 否 | - | 区域标记 |
| body | string | 否 | - | 广告正文关键词 |
| ad_type | string | 否 | - | 广告类型 |
| is_active | string | 否 | - | 是否投放中 |
| start_date | number | 否 | 0 | 开始时间戳，单位秒 |
| end_date | number | 否 | 0 | 结束时间戳，单位秒 |
| active_days_start | number | 否 | - | 投放天数起始 |
| active_days_end | number | 否 | - | 投放天数结束 |
| collation_count_start | number | 否 | - | 广告数起始 |
| collation_count_end | number | 否 | - | 广告数结束 |
| collect_start_date | number | 否 | - | 采集开始时间戳，单位秒 |
| collect_end_date | number | 否 | - | 采集结束时间戳，单位秒 |
| orderBy | string | 否 | update_time | 排序字段 |
| orderType | string | 否 | desc | 排序方式 |
| collation_id | string | 否 | - | 聚合 ID |
| page_id | string | 否 | - | page_id |
| archive_id | string | 否 | - | archive_id |
| product_id | string | 否 | 0 | 按产品 ID 查询 |

---

## 三、响应参数

### 3.1 响应结构

| 字段 | 类型 | 说明 |
|------|------|------|
| count | number | 符合条件的总数 |
| list | array | 广告列表 |
| image_pre | string | 图片前缀 |

### 3.2 主要字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| status | string | 投放状态：`投放中` / `已停止` |
| start_time | string | 开始日期 |
| end_time | string | 结束日期 |
| platform | string | 投放平台 |
| ad_type | string | 广告类型 |
| ad_creative | string | 广告文案 |
| ad_material | string | 素材地址 |
| landing_page_url | string | 落地页 |
| collation_id | string | 聚合 ID |
| archive_id | string | archive ID |
| page_id | string | page ID |
| creative_count | number | 广告数 |
| domain | string | 域名 |
| eu_region | string | 区域标记 |

---

## 四、请求示例

```json
{
  "page": 1,
  "size": 20,
  "link": "example.com",
  "body": "wedding shower",
  "cta_type": "shop now",
  "is_active": 1,
  "start_date": 0,
  "end_date": 0,
  "orderBy": "update_time",
  "orderType": "desc"
}
```

---

## 五、响应示例

```json
{
  "error": {
    "code": 0,
    "message": ""
  },
  "data": {
    "count": 668,
    "image_pre": "http://192.168.7.237:9000",
    "list": [
      {
        "display_format": "DCO",
        "collation_count": 4,
        "collation_id": "2850136788652291",
        "archive_id": "968188512259537",
        "start_date": 1777446000,
        "active_collation_count": 1,
        "total_active_time": null,
        "publisher_platform": [
          "FACEBOOK",
          "INSTAGRAM",
          "AUDIENCE_NETWORK",
          "MESSENGER",
          "THREADS"
        ],
        "body": "",
        "is_aaa_eligible": true,
        "is_active": true,
        "page_id": "498299853562013",
        "cta_type": "SHOP_NOW",
        "link_url": [
          "https://www.hardmandesign.de/collections/mos-collection"
        ],
        "update_time": 1782874744,
        "@timestamp": "2026-07-01T02:59:04.271Z",
        "page_name": "Hardman Design",
        "end_date": null,
        "cards": [
          {
            "body": "Handgefertigte Outdoor Möbel aus Massivholz.\n\nGefertigt aus Eiche, geräucherter Esche oder Iroko, wird jedes Möbelstück auf Bestellung gefertigt und ist für eine langfristige Nutzung im Freien konzipiert.",
            "link_url": "https://www.hardmandesign.de/collections/mos-collection",
            "link_description": null,
            "title": null,
            "cta_text": "Shop Now",
            "cta_type": "SHOP_NOW",
            "media_type": "image",
            "media_img_path": "http://192.168.7.136:9000/facebook/lib_nf/2026/05/01/1777566043_hfccz.jpg"
          }
        ],
        "first_time": 1777446000,
        "total_reach": 493,
        "reach_locations": [
          "DE"
        ],
        "start_date_format": "2026-04-29",
        "end_date_format": "",
        "insert_date_format": "2026-07-01",
        "domain": "www.hardmandesign.de",
        "ad_material": "http://192.168.7.136:9000/facebook/lib_nf/2026/05/01/1777566043_hfccz.jpg",
        "cover_data_list": {
          "20260701": [
            {
              "country": "DE",
              "age_gender_breakdowns": [
                {
                  "age_range": "65+",
                  "male": 18,
                  "female": 25,
                  "unknown": null
                }
              ]
            }
          ]
        },
        "correlation_ad_data": {
          "ad_master_total": 72,
          "ad_product_total": 38
        }
      }
    ]
  }
}
```

### 5.1 响应字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| error.code | number | `0` 表示成功 |
| error.message | string | 错误信息，成功时为空 |
| data.count | number | 符合条件的总记录数 |
| data.list | array | 广告列表 |
| data.image_pre | string | 图片前缀，拼接素材时使用 |

### 5.2 说明

1. 该示例来自 `page_id=498299853562013&page=1&size=1` 的真实返回，`count` 为 `668`。
2. `image_pre` 是素材前缀，`ad_material` 需要结合该前缀理解。
3. `link_url`、`cards`、`publisher_platform`、`reach_locations` 等字段在当前接口中为数组结构。
4. `cover_data_list` 和 `correlation_ad_data` 为接口额外组装的数据。

### 5.3 返回示例字段注释

| 字段 | 注释 |
|------|------|
| `display_format` | 广告展示形式 |
| `collation_count` | 聚合广告数量 |
| `collation_id` | 聚合 ID |
| `archive_id` | 广告归档 ID |
| `start_date` | 开始时间戳 |
| `active_collation_count` | 当前激活聚合数 |
| `total_active_time` | 累计激活时长，可能为空 |
| `publisher_platform` | 投放平台数组 |
| `body` | 广告正文 |
| `is_aaa_eligible` | 区域标记 |
| `is_active` | 是否投放中 |
| `page_id` | Facebook Page ID |
| `cta_type` | CTA 类型 |
| `link_url` | 落地页数组 |
| `update_time` | 更新时间戳 |
| `@timestamp` | ES 索引时间 |
| `page_name` | 页面名称 |
| `end_date` | 结束时间戳，可能为空 |
| `cards` | 广告素材卡片数组 |
| `first_time` | 首次记录时间戳 |
| `total_reach` | 覆盖人数 |
| `reach_locations` | 覆盖地区数组 |
| `start_date_format` | 开始日期格式化结果 |
| `end_date_format` | 结束日期格式化结果 |
| `insert_date_format` | 插入日期格式化结果 |
| `domain` | 域名 |
| `ad_material` | 主要素材地址 |
| `cover_data_list` | 覆盖数据明细 |
| `correlation_ad_data` | 关联广告统计数据 |
