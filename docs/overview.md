# Overview

## Installation

The [miso-sdk](https://pypi.org/project/miso-sdk/) is on [PYPI](https://pypi.org/), you can install `miso-sdk` with the package manager of your choice:

With `pip`:
```shell
$ pip install miso-sdk
```

With `poetry`:
```shell
$ poetry add miso-sdk
```

With `pdm`:
```shell
$ pdm add miso-sdk
```

## Quick Start

To use the SDK, init an `ApiClient` with your API key.
Then you can access Miso APIs with the API client object.

This snippet of code will perform a [search](sdk/search) request, and print the result.

```python
import json
from miso.sdk import ApiClient

api_key = 'YOUR-API-KEY-HERE'

api_client = ApiClient(api_key)
resp = api_client.search.search({"q":"Pouch Bag", "user_id": "MY-ID"})
print(json.dumps(resp, indent=2))
```

Example result:
```json
{
  "message": "success",
  "data": {
    "took": 15,
    "miso_id": "fd3aae82-8068-11ed-89d8-967a8675a919",
    "products": [
      {
        "product_id": "588527603"
      },
      {
        "product_id": "193225388"
      },
      {
        "product_id": "771495105"
      },
      {
        "product_id": "572340793",
      },
      {
        "product_id": "563687627"
      }
    ],
    "total": 65577,
    "start": 0,
    "spellcheck": {
      "spelling_errors": false,
      "auto_spelling_correction": false,
      "original_query": "love",
      "original_query_with_markups": "love",
      "corrected_query": "love",
      "corrected_query_with_markups": "love"
    },
    "product_existence": {},
    "partially_matched_products": null,
    "facet_counts": {
      "facet_fields": {}
    },
    "custom_assets": []
  }
}
```
