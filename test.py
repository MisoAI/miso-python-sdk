import json
import os

from miso.sdk import ApiClient

api_key = os.getenv('API_KEY') or 'bad_api_key'
api_client = ApiClient(api_key)

# resp = api_client.product.read('tmdb-419704')
# resp = api_client.product.delete({'user_ids':['qqd']})
# resp = api_client.user.read('1')
# resp = api_client.user.delete('qqd')

resp = api_client.search.search({"q":"love", "user_id": "cqd"})
# resp = api_client.search.autocomplete({"q":"sta", "user_id": "cqd"})

# resp = api_client.recommendation.product_to_products({"user_id": "cqd", "product_id": "5"})

# resp = api_client.qa.question_answering({"q": "what is ", "min_probability": 0})
# resp = api_client.qa.upload_question_bank({"data": [
#     {"question": "What is python?"},
#     {"question": "What is list comprehension?"},
#     {"question": "How to sort a list in Python?"},
# ]})
# resp = api_client.qa.question_autocomplete({"q": "what is p"})

# resp = api_client.bulk.bulk({"requests":[
#     {
#         "api_name": "qa/question_autocomplete",
#         "body": {
#             "q":"love",
#         }
#     }
# ]})

print(json.dumps(resp))
