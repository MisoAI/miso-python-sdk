import json
import os

from miso.api_client import ApiClient

api_key = os.getenv('API_KEY') or 'bad_api_key'
api_client = ApiClient(api_key)

# resp = api_client.product_read('tmdb-419704')
# resp = api_client.product_delete('qqd')
# resp = api_client.user_read('1')
# resp = api_client.user_delete('qqd')

# resp = api_client.search({"q":"love", "user_id": "cqd"})
resp = api_client.autocomplete({"q":"sta", "user_id": "cqd"})

print(json.dumps(resp))
