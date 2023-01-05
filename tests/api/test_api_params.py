import pytest

from miso.api.bulk import BulkApi
from miso.api.experiment import ExperimentApi
from miso.api.interaction import InteractionApi
from miso.api.product import ProductApi
from miso.api.qa import QAApi
from miso.api.recommendation import RecommendationApi
from miso.api.search import SearchApi
from miso.api.user import UserApi


def make_trap():
    store = dict()

    def trap(
        path: str,
        payload: dict,
        method: str = 'POST',
    ):
        store['path'] = path
        store['payload'] = payload
        store['method'] = method

    return store, trap


SAME = "same_payload_identifier"


params = [
    (
        BulkApi,
        'bulk',
        {"requests":[{"api_name":"search/search", "body": {"q":"star", "user_id": "usr"}}]},
        {"method": "POST", "path": "v1/bulk", "payload": SAME},
    ),
    (
        ExperimentApi,
        'send',
        {"experiment": "some_exp", "user_id": "usr"},
        {"method": "POST", "path": "v1/experiments/some_exp/events", "payload": {"user_id": "usr"}},
    ),
    (
        InteractionApi,
        'upload',
        {"data": [{}]},
        {"method": "POST", "path": "v1/interactions", "payload": SAME},
    ),
    (
        InteractionApi,
        'delete',
        {"user_ids": ["USR1", "USR2", "USR3"]},
        {"method": "DELETE", "path": "v1/interactions", "payload": SAME},
    ),
    (
        ProductApi,
        'upload',
        {"data": [{}]},
        {"method": "POST", "path": "v1/products", "payload": SAME},
    ),
    (
        ProductApi,
        'read',
        {"product_id": "ID0"},
        {"method": "GET", "path": f"v1/products/ID0", "payload": {}},
    ),
    (
        ProductApi,
        'delete',
        {"product_id": "ID0"},
        {"method": "DELETE", "path": f"v1/products/ID0", "payload": {}},
    ),
    (
        QAApi,
        'question_answering',
        {"q": "What is python", "min_probability": 0.3},
        {"method": "POST", "path": f"v1/qa/question_answering", "payload": SAME},
    ),
    (
        QAApi,
        'upload_question_bank',
        {"data": [{}]},
        {"method": "POST", "path": f"v1/qa/questions", "payload": SAME},
    ),
    (
        QAApi,
        'question_autocomplete',
        {"q": "what is wyvern"},
        {"method": "POST", "path": f"v1/qa/question_autocomplete", "payload": SAME},
    ),
    (
        RecommendationApi,
        'user_to_products',
        {"user_id": "usr", "rows": 10},
        {"method": "POST", "path": f"v1/recommendation/user_to_products", "payload": SAME},
    ),
    (
        RecommendationApi,
        'user_to_categories',
        {"user_id": "usr", "rows": 10},
        {"method": "POST", "path": f"v1/recommendation/user_to_categories", "payload": SAME},
    ),
    (
        RecommendationApi,
        'user_to_attributes',
        {"user_id": "usr", "rows": 10, "field": "title"},
        {"method": "POST", "path": f"v1/recommendation/user_to_attributes", "payload": SAME},
    ),
    (
        RecommendationApi,
        'user_to_trending',
        {"user_id": "usr", "rows": 10},
        {"method": "POST", "path": f"v1/recommendation/user_to_trending", "payload": SAME},
    ),
    (
        RecommendationApi,
        'product_to_products',
        {"user_id": "usr", "product_ids":["1701", "1701A"], "rows": 10},
        {"method": "POST", "path": f"v1/recommendation/product_to_products", "payload": SAME},
    ),
    (
        SearchApi,
        'search',
        {"q":"star", "user_id": "usr"},
        {"method": "POST", "path": "v1/search/search", "payload": SAME},
    ),
    (
        SearchApi,
        'autocomplete',
        {"q":"star", "user_id": "usr"},
        {"method": "POST", "path": "v1/search/autocomplete", "payload": SAME},
    ),
    (
        UserApi,
        'upload',
        {"data":[{}]},
        {"method": "POST", "path": "v1/users", "payload": SAME},
    ),
    (
        UserApi,
        'read',
        {"user_id": "ID0"},
        {"method": "GET", "path": f"v1/users/ID0", "payload": {}},
    ),
    (
        UserApi,
        'delete',
        {"user_id": "ID0"},
        {"method": "DELETE", "path": f"v1/users/ID0", "payload": {}},
    ),
]

param_ids = [f"{param[0].__name__}.{param[1]}" for param in params]

@pytest.mark.parametrize('api, func_name, input, expected', params, ids=param_ids)
def test_parameter_passing(api, func_name, input, expected):
    if expected['payload'] == SAME:
        expected['payload'] = {**input} # copy

    store, trap = make_trap()
    api = api(trap)
    func = getattr(api, func_name)

    func(**input)
    assert store == expected

    # Make sure extras works

    expected_extra = {**expected} # copy
    expected_extra['payload']['extra_param'] = 'extra_value'

    func(**input, extra_param="extra_value")
    assert store == expected_extra
