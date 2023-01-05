# MISO SDK for Python

Enhance your site with high conversion magic with [Miso](https://miso.ai/)'s power.

<p>
  <a href="https://pypi.org/project/miso-sdk/"><img src="https://img.shields.io/pypi/v/miso-sdk"></a>
  <a href="https://pypi.org/project/miso-sdk/"><img src="https://img.shields.io/pypi/pyversions/miso-sdk"></a>
  <a href="https://github.com/MisoAI/miso-python-sdk/actions/workflows/testing.yml"><img src="https://github.com/MisoAI/miso-python-sdk/actions/workflows/testing.yml/badge.svg"></a>
  <a href="/LICENSE"><img src="https://img.shields.io/github/license/misoai/miso-python-sdk"></a>
</p>

[Home](https://miso.ai/) |
[Docs](https://docs.miso.ai/) |
[API Reference](https://api.askmiso.com/) |
[Recipes](https://docs.miso.ai/recipes)

## Quick Start
To use the SDK client:

```python
import json
from miso.sdk import ApiClient

api_key = 'YOUR-API-KEY-HERE'

api_client = ApiClient(api_key)
resp = api_client.search.search(q = "love", user_id = "MY-ID")
print(json.dumps(resp, indent=2))
```

will print something similar to:
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

For detailed usage, please refer to [Miso API Document](https://api.askmiso.com/).

## License
This library is distributed under the [MIT license](LICENSE).
