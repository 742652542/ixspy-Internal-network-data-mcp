# Shopify 产品搜索接口文档

## 一、接口概述

| 项目 | 说明 |
|------|------|
| 接口地址 | `http://etsy.int.ixspy.com/api/shopify-goods-all` |
| 请求方式 | POST |
| Content-Type | application/json |
| 接口说明 | 根据多种筛选条件搜索Shopify平台商品信息 |
| 数据限制 | 支持分页查询 |

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
| customized | string | 否 | -1 | 私人定制：`-1`-全部 / `1`-定制 |

### 2.2 文本搜索参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| product_name | string | 商品名称关键词，支持多词搜索（`\|`表示或，`&`表示且） |
| domain | string | 店铺域名 |

### 2.3 分类筛选参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| category_id | string/number | 分类ID |

### 2.4 价格区间参数

| 参数名 | 类型 | 说明 |
|--------|------|------|
| min_price_start | number | 最低价格起始值（美元）|
| min_price_end | number | 最低价格结束值（美元）|

### 2.5 商品上架时间

| 参数名 | 类型 | 说明 |
|--------|------|------|
| created_time_start | number | 商品上架开始时间戳（秒级）|
| created_time_end | number | 商品上架结束时间戳（秒级）|

---

## 三、响应参数

### 3.1 响应结构

```json
{
    "error": {
        "code": 0,
        "message": ""
    },
    "data": {
        "count": 3,
        "list": [...],
        "user_score": []
    }
}
```

**error 字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| code | number | 状态码，0 表示成功 |
| message | string | 错误消息，成功时为空字符串 |

**data 字段说明：**

| 字段 | 类型 | 说明 |
|------|------|------|
| count | number | 符合条件的总记录数 |
| list | array | 商品列表数据 |
| user_score | array | 用户评分数据（暂为空数组）|

---

### 3.2 商品字段说明（list 数组元素）

#### 主要字段

| 字段 | 类型 | 说明 |
|------|------|------|
| product_id | number | 商品ID |
| product_name | string | 商品名称 |
| product_image | string | 商品图片URL |
| shop_id | number | 店铺ID |
| domain | string | 店铺域名 |
| category_id | number | 分类ID |
| ae_category_path | array | AE分类路径数组，如 `[13634, 13657, 13659]` |
| customized | number | 是否定制：`1`-是 / `0`-否 |

#### 价格相关字段

| 字段 | 类型 | 说明 |
|------|------|------|
| min_price | number | 最低价格（美元）|
| max_price | number | 最高价格（美元）|
| currency | string | 货币类型，如 `USD` |

#### 时间相关字段

| 字段 | 类型 | 说明 |
|------|------|------|
| created_time | number | 商品创建时间戳（秒级）|
| update_time | number | 商品更新时间戳（秒级）|
| saled_time | number | 最后销售时间戳（秒级）|
| @timestamp | string | 索引时间戳（ISO 8601格式）|

#### 销量字段

| 字段 | 类型 | 说明 |
|------|------|------|
| sales_total | number | 总销量 |
| search_content | string | 搜索内容 |

#### 详细信息字段 `detail_info`

| 字段 | 类型 | 说明 |
|------|------|------|
| product_id | number | 商品ID |
| product_name | string | 商品名称 |
| shop_id | number | 店铺ID |
| domain | string | 店铺域名 |
| image | string | 商品图片URL |
| category_id | number | 分类ID |
| uri | string | 商品URL路径 |
| sales_total | number | 总销量 |
| created_time | number | 创建时间戳 |
| insert_time | number | 插入时间戳 |
| update_time | number | 更新时间戳 |
| currency | string | 货币类型 |
| min_price | number | 最低价格 |
| max_price | number | 最高价格 |
| instocks_total | number | 库存总数 |
| saled_time | number | 最后销售时间戳 |
| ae_category_path | array | AE分类路径 |
| ae_category_id | number | AE分类ID |

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
    "min_price_start": 0,
    "min_price_end": 0,
    "created_time_start": 0,
    "created_time_end": 0,
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
    "orderBy": "created_time",
    "orderType": "desc",
    "product_name": "necklace&silver",
    "min_price_start": 10,
    "min_price_end": 100
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
    "created_time_start": 1772380800,
    "created_time_end": 1774972800
}
```

### 4.5 多条件组合搜索

```json
{
    "rank_type": "search",
    "customized": "1",
    "page": 1,
    "size": 50,
    "orderBy": "created_time",
    "orderType": "desc",
    "product_name": "dress|skirt",
    "category_id": 0,
    "min_price_start": 20,
    "min_price_end": 200,
    "created_time_start": 1772380800,
    "created_time_end": 1774972800
}
```

---

## 五、响应示例

### 5.1 成功响应

```json
{
    "error": {
        "code": 0,
        "message": ""
    },
    "data": {
        "count": 3,
        "user_score": [],
        "list": [
            {
                "product_id": 9471090360569,
                "shop_id": 401860,
                "update_time": 1775446228,
                "currency": "USD",
                "product_name": "A Line Sweetheart Neck Irregular Taffeta Dark Blue Long Prom Dress KPP2343",
                "min_price": 200,
                "@timestamp": "2026-04-06T03:30:28.348Z",
                "sales_total": 0,
                "domain": "www.kateprom.com",
                "saled_time": 1775446215,
                "created_time": 1774926287,
                "search_content": "www kateprom com",
                "category_id": 0,
                "max_price": 200,
                "ae_category_path": [13634, 13657, 13659],
                "customized": 1,
                "product_image": "https://cdn.shopify.com/s/files/1/0258/7269/5382/files/2026-03-31_101111_473.png?v=1774926538",
                "detail_info": {
                    "product_id": 9471090360569,
                    "product_name": "A Line Sweetheart Neck Irregular Taffeta Dark Blue Long Prom Dress KPP2343",
                    "shop_id": 401860,
                    "domain": "www.kateprom.com",
                    "image": "https://cdn.shopify.com/s/files/1/0258/7269/5382/files/2026-03-31_101111_473.png?v=1774926538",
                    "category_id": 0,
                    "uri": "a-line-sweetheart-neck-irregular-taffeta-dark-blue-long-prom-dress-kpp2343",
                    "sales_total": 0,
                    "created_time": 1774926287,
                    "insert_time": 1775446217,
                    "update_time": 1775446228,
                    "currency": "USD",
                    "min_price": 200,
                    "max_price": 200,
                    "instocks_total": 0,
                    "saled_time": 1775446215,
                    "ae_category_path": [13634, 13657, 13659],
                    "ae_category_id": 13659
                }
            }
        ]
    }
}
```

### 5.2 错误响应

```json
{
    "error": {
        "code": 400,
        "message": "参数错误"
    },
    "data": null
}
```

---

## 六、错误码说明

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

---

## 七、附录

### 7.1 排序字段枚举

| 字段 | 说明 |
|------|------|
| created_time | 创建时间（默认）|
| ads_7_count | 7日广告指数 |
| ads_30_count | 30日广告指数 |

---

### 7.2 商品名搜索说明

- **单关键词：** `"dress"` 搜索包含 dress 的商品
- **或关系：** `"dress|skirt"` 搜索包含 dress 或 skirt 的商品
- **且关系：** `"dress&summer"` 搜索同时包含 dress 和 summer 的商品
- **组合：** `"dress|skirt&summer"` 搜索包含(dress 或 skirt)且包含 summer 的商品

---

### 7.3 时间戳说明

- **时间戳格式：** Unix 时间戳，单位为秒
- **示例：** `1774926287` 表示 `2026-03-28 00:00:00` 左右
- **转换工具：** 可使用在线时间戳转换器或编程语言内置函数

---

### 7.4 AE分类路径说明

`ae_category_path` 是一个数组，表示商品的分类层级路径：

```json
"ae_category_path": [13634, 13657, 13659]
```

- 第一个元素：一级分类
- 第二个元素：二级分类
- 第三个元素：三级分类（末级分类）

---

### 7.5 使用建议

1. **分页建议：**
   - 建议每页条数：20、50、100
   - 默认按 `created_time` 降序排列

2. **性能优化：**
   - 建议先使用 `product_name` 或 `domain` 缩小范围
   - 再添加其他筛选条件

3. **价格筛选：**
   - 使用 `min_price_start` 和 `min_price_end` 设置价格区间
   - 值为 0 表示不限制

4. **定制商品筛选：**
   - `customized`: `-1` 表示查询所有商品
   - `customized`: `1` 表示仅查询定制商品

---

### 7.6 完整参数列表

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| rank_type | string | search | 排名类型 |
| customized | string | -1 | 私人定制：`-1`-全部 / `1`-定制 |
| page | number | 1 | 页码 |
| size | number | 20 | 每页条数 |
| orderBy | string | created_time | 排序字段 |
| orderType | string | desc | 排序方式 |
| product_name | string | - | 商品名称 |
| category_id | string/number | - | 分类ID |
| domain | string | - | 域名 |
| min_price_start | number | 0 | 最低价格起始值 |
| min_price_end | number | 0 | 最低价格结束值 |
| created_time_start | number | 0 | 商品创建开始时间戳 |
| created_time_end | number | 0 | 商品创建结束时间戳 |

---

### 7.7 参数使用示例

#### 价格筛选示例

```json
{
    "min_price_start": 10,
    "min_price_end": 100
}
```
筛选价格在 $10-$100 之间的商品

#### 时间范围筛选示例

```json
{
    "created_time_start": 1772380800,
    "created_time_end": 1774972800
}
```
筛选创建时间在指定范围内的商品

#### 定制商品筛选示例

```json
{
    "customized": "1"
}
```
仅筛选定制商品

---

**文档版本：** v1.1  
**最后更新：** 2026-04-07