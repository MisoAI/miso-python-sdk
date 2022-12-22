# `ApiClient.search`

The Search API provides personalized, typo-correcting, semantic search for your site. You send this API the search queries users entered, and the API returns the relevant search results tailored to your users' interests.

----------------------------------------------------------------------

## `ApiClient.search.search()`
Perform a personalized, typo-correcting, semantic search.

### Syntax
```python
response = api_client.search.search(payload)
```

### Payload

`payload` is a dictionary contains all the parameters that will be passed to Miso REST API.

Here are some often used parameters:

| Name           | Type      | Description |
| -------------- | --------- | ----------- |
| `q`            | str       | The search query the user has entered. |
| `user_id`      | str       | The user who made the query and for whom Miso will personalize the results. Either user_id or anonymous_id needs to be specified. |
| `anonymous_id` | str       | The anonymous visitor who made the query and for whom Miso will personalize the results. Either user_id or anonymous_id needs to be specified for personalization to work. |
| `fl`           | list[str] | List of fields to retrieve. `product_id` is always included. When not specified, only `product_id` will be retrieved. |
| `fq`           | str       | Filter query result, in Solr syntax. |
| `boost_fq`     | str       | Boost some of matched products, in Solr syntax. |
| `start`        | int       | The offset of records to retrieve. |
| `rows`         | int       | Number of records to retrieve. |


### Return Value

A dictionary of returned result with following properties:

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| `products`     | list[dict] | A list of Product records. Use `fl` parameter to specify what fields are returned. |
| `start`        | int        | The offset of records to retrieve. |
| `total`        | int        | The total number of matched records. |


### Example
```python
payload = {
  "user_id": "...",
  "q": "doge",
  "fl": ["title", "sale_price", "custom_attributes.author"],
}

response = api_client.search.search(payload)
products = response["products"]
```

----------------------------------------------------------------------

## `ApiClient.search.autocomplete()`

Provides real-time, personalized, typo resistant typeahead for your search bar.

### Syntax
```python
response = api_client.search.autocomplete(payload)
```

### Payload

`payload` is a dictionary contains all the parameters that will be passed to Miso REST API.

Here are some often used parameters:

| Name                | Type      | Description |
| ------------------- | --------- | ----------- |
| `q`                 | str       | The search query the user has entered. |
| `user_id`           | str       | The user who made the query and for whom Miso will personalize the results. Either user_id or anonymous_id needs to be specified. |
| `anonymous_id`      | str       | The anonymous visitor who made the query and for whom Miso will personalize the results. Either user_id or anonymous_id needs to be specified for personalization to work. |
| `completion_fields` | list[str] | Specify the fields used for autocompletion. Use `["title"]` by default. |
| `fl`                | list[str] | List of fields to retrieve. `product_id` is always included. When not specified, only `product_id` will be retrieved. |
| `start`             | int       | The offset of records to retrieve. |
| `rows`              | int       | Number of records to retrieve. |



### Return Value

A dictionary of returned result with following properties:

| Name           | Type            | Description |
| -------------- | --------------- | ----------- |
| `completions`  | dict[str, list] | A dictionary with autocompleted field as key, and list of autocomplete result as it's value. |

### Example
```python
payload = {
  "user_id": "...",
  "q": "doge",
  "fl": ["title", "sale_price"],
  "completion_fields": ["title", "tags", "custom_attributes.author"],
}

response = api_client.search.autocomplete(payload)
products = response["completions"]
```

----------------------------------------------------------------------

## `ApiClient.search.multi_get()`

provides a simple and fast interface to retrieve products by their product ids.

### Syntax
```python
response = api_client.search.multi_get(product_ids)
```

### Payload

`payload` is a dictionary contains all the parameters that will be passed to Miso REST API.

Here are some often used parameters:

| Name                | Type      | Description |
| ------------------- | --------- | ----------- |
| `product_ids`       | list[str] | List of product ids to retrive. |
| `fl`                | list[str] | List of fields to retrieve. `product_id` is always included. When not specified, all fields will be retrieved. |

### Return Value

A dictionary of returned result with following properties:

| Name           | Type            | Description |
| -------------- | --------------- | ----------- |
| `products`     | list[dict]      | A list of Product records. Use `fl` parameter to specify what fields are returned. |

### Example
```python
payload = {
  "user_id": "...",
  "product_ids":[
    "765881384",
    "1021528795",
    "741362619",
  ]
  "fl": ["title", "sale_price"],
}

response = api_client.search.multi_get(payload)
products = response["products"]
```

----------------------------------------------------------------------

## Learn more
For advanced usage and extra parameters, see [REST API](https://api.askmiso.com/#tag/Search-APIs) for detail.
