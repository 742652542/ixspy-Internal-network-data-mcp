# Facebook 公开查询接口 - 广告产品列表

## 一、接口概述

| 项目 | 说明 |
|------|------|
| 接口地址 | `http://etsy.int.ixspy.com/api/facebook/public/ad-products` |
| 请求方式 | GET |
| Content-Type | application/json |
| 接口说明 | 根据分类、关键词、域名和时间范围查询 Facebook 广告产品 |
| 数据限制 | 支持分页查询 |

---

## 二、请求参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| page | number | 否 | 1 | 页码 |
| size | number | 否 | 20 | 每页条数 |
| category_id | string/number | 否 | - | 分类 ID |
| product_name | string | 否 | - | 商品名称关键词 |
| source_content | string | 否 | - | 文案内容关键词，支持 `|` 或 `&` 组合搜索 |
| domain | string | 否 | - | 域名 |
| created_time_start | number | 否 | 0 | 开始时间戳，单位秒 |
| created_time_end | number | 否 | 0 | 结束时间戳，单位秒 |
| orderBy | string | 否 | update_time | 排序字段 |
| orderType | string | 否 | desc | 排序方式 |

---

## 三、响应参数

### 3.1 响应结构

| 字段 | 类型 | 说明 |
|------|------|------|
| count | number | 符合条件的总数 |
| list | array | 广告产品列表 |

### 3.2 主要字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| link_id | number/string | 链接 ID |
| archive_id | number/string | 广告归档 ID |
| link_domain | string | 域名 |
| source_content | string | 广告内容 |
| category_id | number/string | 分类 ID |
| update_time | number | 更新时间戳 |

---

## 四、请求示例

```json
{
  "page": 1,
  "size": 20,
  "category_id": "",
  "product_name": "dress",
  "source_content": "wedding&shower|bride&shower",
  "domain": "example.com",
  "created_time_start": 0,
  "created_time_end": 0,
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
    "count": 9327003,
    "list": [
      {
        "type": "",
        "link_url": "https://www.grupogen.com.br/curso-online-dominando-legal-ops-luis-gustavo-potrick-duarte-gen-6442230993682/",
        "currency": "",
        "page_id": 241966022895906,
        "source_content": "www.grupogen.com.br ### Mastering Legal Ops online course with Gustavo Potrick |GEN Group ### Find the best books, e-books and scientific, technical and professional courses from the publishers Method, Forense, Guanabara Koogan, Roca, Santos, Atlas and LTC.",
        "price": 0,
        "link_id": "406c8d94b3a851411f551fe91cc685e1",
        "link_domain": "www.grupogen.com.br",
        "lang": "pt",
        "title": "Mastering Legal Ops online course with Gustavo Potrick |GEN Group",
        "category_id": 121,
        "image": "https://mktgen.com.br/imagens/curso-dominando-legal-ops/thumb.png",
        "update_time": 1782875888
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
| data.list | array | 广告产品列表，分页返回 |

### 5.2 说明

1. `count` 为符合条件的总记录数，当前真实返回值为 `9327003`。
2. `list[0]` 是实际接口返回的广告产品样例。
3. `source_content` 为广告正文/搜索内容，支持关键词筛选。
4. `category_id`、`domain`、`product_name` 等条件可以组合使用。
5. 返回字段来自 ES 索引，字段可能因数据源不同而变化。

### 5.3 返回示例字段注释

| 字段 | 注释 |
|------|------|
| `type` | 广告类型标识，当前示例为空 |
| `link_url` | 广告落地页链接 |
| `currency` | 币种，当前示例为空 |
| `page_id` | Facebook Page ID |
| `source_content` | 广告正文内容，用于关键词搜索 |
| `price` | 价格，当前示例为 `0` |
| `link_id` | 链接 ID，ES 数据主键样式 |
| `link_domain` | 链接域名 |
| `lang` | 语言 |
| `title` | 广告标题 |
| `category_id` | 分类 ID |
| `image` | 图片地址 |
| `update_time` | 更新时间戳 |
