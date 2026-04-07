# Shopify 产品搜索接口文档

## 一、接口概述

| 项目 | 说明                                                |
|------|---------------------------------------------------|
| 接口地址 | `http://etsy.int.ixspy.com/api/shopify-goods-all` |
| 请求方式 | POST                                              |
| Content-Type | application/json                                  |
| 接口说明 | 根据多种筛选条件搜索Shopify平台商品信息                           |
| 数据限制 | 支持分页查询                                            |

---

## 二、请求参数

### 2.1 基础参数

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| page | number | 否 | 1 | 页码 |
| size | number | 否 | 20 | 每页条数 |
| orderBy | string | 否 | created_time | 排序字段，见[排序字段枚举](#71-排序字段枚举) |
| orderType | string | 否 | desc | 排序方式：`desc`-降序 / `asc`-升序 |
| rank_type | string | 否 | search | 排名类型 |
| customized | string | 否 | -1 | 自定义标识 |

### 2.2 文本搜索参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| product_name | string | 商品名称关键词，支持多词搜索（`\|`表示或，`&`表示且） |
| domain | string | 店铺域名 |
| shop_id | string | 店铺ID |

### 2.3 分类筛选参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| category_id | string | 分类ID |

### 2.4 价格区间参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| min_price_start | number | 最低价格起始值（美元）|
| min_price_end | number | 最低价格结束值（美元）|

### 2.5 销量指数参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| sales_7_count_start | number | 7天销量指数起始值 |
| sales_7_count_end | number | 7天销量指数结束值 |

### 2.6 时间筛选参数

#### 最后销售时间

| 参数名 | 类型 | 说明 |
|--------|------|------|
| saled_time_start | number | 最后销售开始时间戳（秒级）|
| saled_time_end | number | 最后销售结束时间戳（秒级）|

#### 商品创建时间

| 参数名 | 类型 | 说明 |
|--------|------|------|
| created_time_start | number | 商品创建开始时间戳（秒级）|
| created_time_end | number | 商品创建结束时间戳（秒级）|
| created_time | array | 创建时间范围数组 |

#### 商品更新时间

| 参数名 | 类型 | 说明 |
|--------|------|------|
| update_time_start | number | 商品更新开始时间戳（秒级）|
| update_time_end | number | 商品更新结束时间戳（秒级）|

---

## 三、响应参数

### 3.1 响应结构

| 字段 | 类型 | 说明 |
|------|------|------|
| code | number | 状态码，0 表示成功 |
| message | string | 响应消息 |
| data | object | 响应数据 |

**data 字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| count | number | 符合条件的总记录数 |
| list | array | 商品列表数据 |

---

### 3.2 商品字段说明（list 数组元素）

| 字段 | 类型 | 说明 |
|------|------|------|
| product_id | string | 商品ID |
| product_name | string | 商品名称 |
| domain | string | 店铺域名 |
| shop_id | string | 店铺ID |
| category_id | string | 分类ID |
| min_price | number | 最低价格 |
| created_time | number | 创建时间戳（秒级）|
| update_time | number | 更新时间戳（秒级）|
| sales_7_count | number | 7天销量指数 |
| saled_time | number | 最后销售时间戳 |

---

## 四、请求示例

### 4.1 基础搜索

```json
{
    "rank_type": "search",
    "customized": "-1",
    "page": 1,
    "size": 20,
    "orderBy": "created_time",
    "orderType": "desc",
    "product_name": "dress",
    "category_id": "",
    "shop_id": "",
    "min_price_start": 0,
    "min_price_end": 0,
    "sales_7_count_start": 0,
    "sales_7_count_end": 0,
    "saled_time_start": 0,
    "saled_time_end": 0,
    "created_time_start": 0,
    "created_time_end": 0,
    "update_time_start": 0,
    "update_time_end": 0,
    "created_time": [],
    "domain": ""
}
```

### 4.2 按关键词和价格搜索

```json
{
    "rank_type": "search",
    "customized": "-1",
    "page": 1,
    "size": 20,
    "orderBy": "sales_7_count",
    "orderType": "desc",
    "product_name": "necklace&silver",
    "min_price_start": 10,
    "min_price_end": 100,
    "sales_7_count_start": 50,
    "sales_7_count_end": 500
}
```

### 4.3 按域名搜索

```json
{
    "rank_type": "search",
    "customized": "-1",
    "page": 1,
    "size": 20,
    "orderBy": "created_time",
    "orderType": "desc",
    "domain": "example.myshopify.com"
}
```

### 4.4 按时间范围搜索

```json
{
    "rank_type": "search",
    "customized": "-1",
    "page": 1,
    "size": 20,
    "orderBy": "created_time",
    "orderType": "desc",
    "created_time_start": 1672531200,
    "created_time_end": 1704067200,
    "saled_time_start": 1703980800,
    "saled_time_end": 1704067200
}
```

### 4.5 多条件组合搜索

```json
{
    "rank_type": "search",
    "customized": "-1",
    "page": 1,
    "size": 50,
    "orderBy": "sales_7_count",
    "orderType": "desc",
    "product_name": "dress|skirt",
    "category_id": "123",
    "shop_id": "shop_001",
    "min_price_start": 20,
    "min_price_end": 200,
    "sales_7_count_start": 100,
    "sales_7_count_end": 1000,
    "created_time_start": 1672531200,
    "created_time_end": 1704067200
}
```

---

## 五、响应示例

### 5.1 成功响应

```json
{
    "code": 0,
    "message": "success",
    "data": {
        "count": 1580,
        "list": [
            {
                "product_id": "123456789",
                "product_name": "Women Summer Dress - Casual Beach Wear",
                "domain": "example.myshopify.com",
                "shop_id": "shop_001",
                "category_id": "123",
                "min_price": 29.99,
                "created_time": 1672531200,
                "update_time": 1704067200,
                "sales_7_count": 320,
                "saled_time": 1703980800,
                "image_url": "https://cdn.shopify.com/...",
                "product_url": "https://example.myshopify.com/products/..."
            },
            {
                "product_id": "987654321",
                "product_name": "Vintage Necklace - Handmade Jewelry",
                "domain": "jewelry-boutique.myshopify.com",
                "shop_id": "shop_002",
                "category_id": "456",
                "min_price": 49.99,
                "created_time": 1672617600,
                "update_time": 1704153600,
                "sales_7_count": 185,
                "saled_time": 1704067200,
                "image_url": "https://cdn.shopify.com/...",
                "product_url": "https://jewelry-boutique.myshopify.com/products/..."
            }
        ]
    }
}
```

### 5.2 错误响应

```json
{
    "code": 10001,
    "message": "参数错误",
    "data": null
}
```

---

## 六、错误码说明

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 10001 | 参数错误 |
| 10002 | 时间参数无效 |
| 10003 | 未授权 |
| 10004 | 请求频率超限 |
| 50000 | 服务器内部错误 |

---

## 七、附录

### 7.1 排序字段枚举

| 字段 | 说明 |
|------|------|
| created_time | 创建时间（默认）|
| sales_7_count | 7天销量指数 |
| min_price | 最低价格 |
| update_time | 更新时间 |

---

### 7.2 商品名搜索说明

- **单关键词：** `"dress"` 搜索包含 dress 的商品
- **或关系：** `"dress|skirt"` 搜索包含 dress 或 skirt 的商品
- **且关系：** `"dress&summer"` 搜索同时包含 dress 和 summer 的商品
- **组合：** `"dress|skirt&summer"` 搜索包含(dress 或 skirt)且包含 summer 的商品

---

### 7.3 时间戳说明

- **时间戳格式：** Unix 时间戳，单位为秒
- **示例：** `1704067200` 表示 `2024-01-01 00:00:00 UTC`
- **转换工具：** 可使用在线时间戳转换器或编程语言内置函数

---

### 7.4 使用建议

1. **分页建议：**
   - 建议每页条数：20、50、100
   - 默认按 `created_time` 降序排列

2. **性能优化：**
   - 建议先使用 `product_name` 或 `domain` 缩小范围
   - 再添加其他筛选条件

3. **价格筛选：**
   - 使用 `min_price_start` 和 `min_price_end` 设置价格区间
   - 值为 0 表示不限制

4. **销量筛选：**
   - 使用 `sales_7_count_start` 和 `sales_7_count_end` 设置销量区间
   - 值为 0 表示不限制

---

### 7.5 完整参数列表

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| rank_type | string | search | 排名类型 |
| customized | string | -1 | 自定义标识 |
| page | number | 1 | 页码 |
| size | number | 20 | 每页条数 |
| orderBy | string | created_time | 排序字段 |
| orderType | string | desc | 排序方式 |
| product_name | string | - | 商品名称 |
| category_id | string | - | 分类ID |
| shop_id | string | - | 店铺ID |
| domain | string | - | 域名 |
| min_price_start | number | 0 | 最低价格起始值 |
| min_price_end | number | 0 | 最低价格结束值 |
| sales_7_count_start | number | 0 | 7天销量指数起始值 |
| sales_7_count_end | number | 0 | 7天销量指数结束值 |
| saled_time_start | number | 0 | 最后销售开始时间戳 |
| saled_time_end | number | 0 | 最后销售结束时间戳 |
| created_time_start | number | 0 | 商品创建开始时间戳 |
| created_time_end | number | 0 | 商品创建结束时间戳 |
| update_time_start | number | 0 | 商品更新开始时间戳 |
| update_time_end | number | 0 | 商品更新结束时间戳 |
| created_time | array | [] | 创建时间范围数组 |

---

### 7.6 参数使用示例

#### 价格筛选示例

```json
{
    "min_price_start": 10,
    "min_price_end": 100
}
```
筛选价格在 $10-$100 之间的商品

#### 销量筛选示例

```json
{
    "sales_7_count_start": 50,
    "sales_7_count_end": 500
}
```
筛选7天销量指数在 50-500 之间的商品

#### 时间范围筛选示例

```json
{
    "created_time_start": 1672531200,
    "created_time_end": 1704067200
}
```
筛选创建时间在 2023-01-01 到 2024-01-01 之间的商品

#### 组合筛选示例

```json
{
    "product_name": "dress",
    "min_price_start": 20,
    "min_price_end": 200,
    "sales_7_count_start": 100,
    "sales_7_count_end": 1000,
    "created_time_start": 1672531200,
    "created_time_end": 1704067200,
    "orderBy": "sales_7_count",
    "orderType": "desc"
}
```
综合筛选：商品名包含 dress，价格 $20-$200，销量指数 100-1000，创建时间 2023年内，按销量降序排列

---

**文档版本：** v1.0  
**最后更新：** 2026-04-07