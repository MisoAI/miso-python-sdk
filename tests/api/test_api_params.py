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


params = [
    (
        BulkApi,
        'bulk',
        {"requests":[{"api_name":"search/search", "body": {"q":"star", "user_id": "usr"}}]},
        {"path": "v1/bulk"},
    ),
    (
        ExperimentApi,
        'send',
        {"experiment": "some_exp", "user_id": "usr"},
        {"path": "v1/experiments/some_exp/events", "payload": {"user_id": "usr"}},
    ),
    (
        InteractionApi,
        'upload',
        {"data": [{}]},
        {"path": "v1/interactions"},
    ),
    (
        InteractionApi,
        'delete',
        {"user_ids": ["USR1", "USR2", "USR3"]},
        {"method": "DELETE", "path": "v1/interactions"},
    ),
    (
        ProductApi,
        'upload',
        {"data": [{}]},
        {"path": "v1/products"},
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
        {"path": f"v1/qa/question_answering"},
    ),
    (
        QAApi,
        'upload_question_bank',
        {"data": [{}]},
        {"path": f"v1/qa/questions"},
    ),
    (
        QAApi,
        'question_autocomplete',
        {"q": "what is wyvern"},
        {"path": f"v1/qa/question_autocomplete"},
    ),
    (
        RecommendationApi,
        'user_to_products',
        {"user_id": "usr", "rows": 10},
        {"path": f"v1/recommendation/user_to_products"},
    ),
    (
        RecommendationApi,
        'user_to_categories',
        {"user_id": "usr", "rows": 10},
        {"path": f"v1/recommendation/user_to_categories"},
    ),
    (
        RecommendationApi,
        'user_to_attributes',
        {"user_id": "usr", "rows": 10, "field": "title"},
        {"path": f"v1/recommendation/user_to_attributes"},
    ),
    (
        RecommendationApi,
        'user_to_trending',
        {"user_id": "usr", "rows": 10},
        {"path": f"v1/recommendation/user_to_trending"},
    ),
    (
        RecommendationApi,
        'product_to_products',
        {"user_id": "usr", "product_ids":["1701", "1701A"], "rows": 10},
        {"path": f"v1/recommendation/product_to_products"},
    ),
    (
        SearchApi,
        'search',
        {"q":"star", "user_id": "usr"},
        {"path": "v1/search/search"},
    ),
    (
        SearchApi,
        'autocomplete',
        {"q":"star", "user_id": "usr"},
        {"path": "v1/search/autocomplete"},
    ),
    (
        UserApi,
        'upload',
        {"data":[{}]},
        {"path": "v1/users"},
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
@pytest.mark.local
def test_parameter_passing(api, func_name, input, expected):

    # set default values
    default_expected = {
        "method": "POST",
        "payload": {**input}, # copy
    }
    expected = {**default_expected, **expected}

    # make api client with trap set
    store, trap = make_trap()
    api = api(trap)
    func = getattr(api, func_name)

    # check parameter passing is correct
    func(**input)
    assert store == expected

    # Make sure extras works
    expected_extra = {**expected} # copy
    expected_extra['payload']['extra_param'] = 'extra_value'

    func(**input, extra_param="extra_value")
    assert store == expected_extra
