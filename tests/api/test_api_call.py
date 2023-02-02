import os

import pytest

from miso.api.bulk import BulkApi
from miso.api.experiment import ExperimentApi
from miso.api.interaction import InteractionApi
from miso.api.product import ProductApi
from miso.api.qa import QAApi
from miso.api.recommendation import RecommendationApi
from miso.api.search import SearchApi
from miso.api.user import UserApi
from miso.sdk import ApiClient

from ..utils import schema_checker


schema_full_product = {
    "product_id": str,
    "url": str,
    "title": str,
}

schema_simple_product = {"product_id": str}

schema_searched_product = {
    "product_id": str,
    "_boosted": bool,
}

schema_search = {
    "took": int,
    "total": int,
    "start": int,
    "products":[schema_searched_product],
}

schema_qa = {
    "total": int,
    "took": int,
    "answers": [{
        "product_id": str,
        "answer": {
            "text": str,
        },
    }]
}

schema_qa_complete = {
    "took": int,
    "completions": [{
        "question": str,
        "weight": float,
    }]
}

schema_2i = {
    "took": int,
    "products": [schema_simple_product]
}

schema_2t = schema_2i

schema_2c = {
    "took": int,
    "categories": [{
        "category": [str],
        "recommended_products": [schema_simple_product]
    }]
}

schema_2a = {
    "took": int,
    "attributes": [{
        "value": str,
        "recommended_products": [schema_simple_product]
    }]
}

schema_autocomplete = {
    "took": int,
    "completions": {
        "*": [{
            "text": str,
            "text_with_markups": str,
            "text_with_inverted_markups": str,
            "product": schema_searched_product,
        }]
    }
}

schema_user = {
    "user_id": str,
    "name": str,
}

schema_mget = {
    "took": int,
    "products": [schema_simple_product]
}

schema_ack = {"message": str}

def make_bulk_schema(schema:dict):
    return [{
        "error": bool,
        "status_code": int,
        "body":{
            "data": schema,
        },
    }]

params = [
    (
        BulkApi,
        'bulk',
        {"requests":[{"api_name":"search/search", "body": {"q":"star", "user_id": "usr"}}]},
        make_bulk_schema(schema_search),
    ),
    # (
    #     ExperimentApi,
    #     'send',
    #     {"experiment": "some_exp", "user_id": "usr"},
    #     None,
    # ),
    # (
    #     InteractionApi,
    #     'upload',
    #     {"data": [{}]},
    #     None,
    # ),
    # (
    #     InteractionApi,
    #     'delete',
    #     {"user_ids": ["USR1", "USR2", "USR3"]},
    #     None,
    # ),
    # (
    #     ProductApi,
    #     'upload',
    #     {"data": [{}]},
    #     None,
    # ),
    (
        ProductApi,
        'read',
        {"product_id": "184973030"},
        schema_full_product,
    ),
    # (
    #     ProductApi,
    #     'delete',
    #     {"product_id": "ID0"},
    #     None,
    # ),
    # (
    #     QAApi,
    #     'upload_question_bank',
    #     {"data": [
    #         {"question": "What is python?"},
    #         {"question": "What is list comprehension?"},
    #         {"question": "How to sort a list in Python?"}
    #     ]},
    #     schema_ack,
    # ),
    (
        QAApi,
        'question_answering',
        {"q": "What is python", "min_probability": 0.3},
        schema_qa,
    ),
    (
        QAApi,
        'question_autocomplete',
        {"q": "what is wyvern"},
        schema_qa_complete,
    ),
    (
        RecommendationApi,
        'user_to_products',
        {"user_id": "usr", "rows": 10},
        schema_2i,
    ),
    (
        RecommendationApi,
        'user_to_categories',
        {"user_id": "usr", "rows": 10},
        schema_2c,
    ),
    (
        RecommendationApi,
        'user_to_attributes',
        {"user_id": "usr", "rows": 10, "field": "title"},
        schema_2a,
    ),
    (
        RecommendationApi,
        'user_to_trending',
        {"user_id": "usr", "rows": 10},
        schema_2t,
    ),
    (
        RecommendationApi,
        'product_to_products',
        {"user_id": "usr", "product_ids":["1701", "1701A"], "rows": 10},
        schema_2i,
    ),
    (
        SearchApi,
        'search',
        {"q":"star", "user_id": "usr"},
        schema_search,
    ),
    (
        SearchApi,
        'autocomplete',
        {"q":"star", "user_id": "usr"},
        schema_autocomplete,
    ),
    (
        SearchApi,
        'multi_get',
        {"product_ids":[""], "user_id": "usr"},
        schema_mget,
    ),
    # (
    #     UserApi,
    #     'upload',
    #     {"data":[{}]},
    #     schema_ack,
    # ),
    (
        UserApi,
        'read',
        {"user_id": "eerbstoesser"},
        schema_user,
    ),
    # (
    #     UserApi,
    #     'delete',
    #     {"user_id": "ID0"},
    #     schema_ack,
    # ),
]

param_ids = [f"{param[0].__name__}.{param[1]}" for param in params]

@pytest.mark.parametrize('api, func_name, input, schema', params, ids=param_ids)
def test_api_call(api, func_name, input, schema):
    api_key = os.getenv('API_KEY')
    assert api_key, "Env `API_KEY` must be set to run the test"

    api_client = api(ApiClient(api_key)._api_call)
    func = getattr(api_client, func_name)

    response = func(**input)
    print(response)
    schema_checker(schema, response)
