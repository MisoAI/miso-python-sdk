# `ApiClient.product`

Miso's Product / Content APIs let you upload, read, and delete Product / Content records that represent your site's catalog.

----------------------------------------------------------------------

## `ApiClient.product.upload()`

Insert multiple product / content records.

A "Product" can be:
- Physical goods for sale
- An article on your site
- A song
- Any thing with it's own ID and other metadata that need be searched.


### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")

products = [
  # First product
  {
    "product_id": "arizona-ginseng-honey",
    "title": "Arizona, Green Tea with Ginseng & Honey",
    "description": "Hand picked by experienced farmer, the Arizona Green Tea with Ginseng & Honey is the best choice for you to get a taste of calm and peace." ,
    "categories": [
        ["Food", "Beverages", "Tea", "Green Tea"],
        ["Food", "Domestic", "Arizona"],

    ],
    "cover_image": "https://example.com/path/to/image.jpg",
  },
  # Second product
  {
    "product_id": "31fdd0d",
    "title": "Embroidered Silly Goose Sweatshirt, Funny Sweatshirt",
    "description": "This embroidered Silly Goose sweatshirt is super soft and cozy. Perfect to lounge around, run errands, or walk your dog." ,
    "categories": [
        ["Clothing", "Womens Clothing", "Womens Sweaters"],
    ],
    "cover_image": "https://example.com/path/to/image.jpg",
  },
]

api_client.product.upload(data=products)
```

### Parameters

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `data`         | dict       | List of product / content records. |


`data` is a list of dictionaries, each dictionary represents a product or content record.

Often used fields are:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `product_id`   | str        | Required. ID of the product being uploaded. |
| `title`        | str        | Title or name of the product. |
| `description`  | str        | Detail description for the product. |
| `html`         | str        | The HTML content of the product. |
| `type`         | str        | Type of the product. For example, a travel site may have `flight` and `hotel` sales. |
| `categories`   | list[list[str]] | Hierarchical categories for the product. Multiple category path can be assigned. |
| `tags`         | list[str]  | The tags that have been associated with the product. |
| `url`          | str        | URL to product page. |
| `cover_image`  | str        | URL to main product / content image. |
| `brand`        | str        | Brand name for the product. Ex: `Nike`, `Disney`, `Kirkland`. |
| `authors`      | list[str]  | Author(s) of the content. An article or book may have multiple authors. |
| `custom_attributes` | dict  | A collection of key-value pair that can store arbitrary values. Useful if you want to use fields that are not defined in REST API spec. <br><br>Key must be a string. and value can be a `bool`, a `str`, a `number`, a `list`, or `None` |

Please refer to [REST API document](https://api.askmiso.com/#tag/Product-Content-APIs) for complete field list. With more detailed and accurate metadata provided, Miso can yield better search result for your customers.

### Return Value

A dictionary of returned result with following properties:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `errors`       | bool       | Upload successed or failed. |
| `message`      | str        | Summarized message. |
| `data`         | list[str]  | Detail for each error happend. |

----------------------------------------------------------------------


## `ApiClient.product.read()`

Read a single product / content record by `product_id`.

### Example

```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")
response = api_client.product.read(product_id='arizona-ginseng-honey')
product_data = response['data']
```

### Parameters

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `product_id`   | str        | ID of the product |

### Return Value

Returned value is a dict with all fields from product data.

Should cantain all data uploaded with `ApiClient.product.upload()`


## `ApiClient.product.delete()`

Remove a product from catalog.

### Example
```python
from miso.sdk import ApiClient

api_client = ApiClient(api_key="{api_key}")
api_client.product.delete(product_id='arizona-ginseng-honey')
```

### Parameters
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `product_id`   | str        | ID of the product to be removed. |

### Return Value
| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `message`      | str        | Execution result message. |


## Learn more
For advanced usage and extra parameters, see [REST API](https://api.askmiso.com/#tag/Product-Content-APIs) for detail.
