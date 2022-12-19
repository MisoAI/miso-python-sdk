# MISO SDK for Python

Enhance your site with high conversion magic with [Miso's](https://miso.ai/) power.

<p>
  <a href="/LICENSE"><img src="https://img.shields.io/npm/l/@miso.ai/client-sdk"></a>
</p>

[Home](https://miso.ai/) |
[Docs](https://docs.miso.ai/) |
[API Reference](https://api.askmiso.com/) |
[Recipes](https://docs.miso.ai/recipes)

## Quick Start
To use the SDK client:

```python
from miso.sdk import ApiClient

api_key = 'YOUR-API-KEY-HERE'

api_client = ApiClient(api_key)
resp = api_client.search.search({"q":"love", "user_id": "MY-ID"})
print(resp)
```

will print:
```json
{"message":"success","data":{"took":793,"miso_id":"0c4bd428-7f60-11ed-b82d-4ad9871739bd","products":[{"product_id":"936776","product_group_id":"921757"},{"product_id":"73968","product_group_id":"816372"},{"product_id":"8204005","product_group_id":"13051038"},{"product_id":"29762367","product_group_id":"50123221"},{"product_id":"1275404","product_group_id":"1264375"}],"total":23368,"start":0,"spellcheck":{"spelling_errors":false,"auto_spelling_correction":false,"original_query":"love","original_query_with_markups":"love","corrected_query":"love","corrected_query_with_markups":"love"},"product_existence":{},"partially_matched_products":null,"facet_counts":{"facet_fields":{}},"custom_assets":[]}}
```

For detailed usage, please refert to [Miso API Document](https://api.askmiso.com/).

## License
This library is distributed under the [MIT license](LICENSE).
