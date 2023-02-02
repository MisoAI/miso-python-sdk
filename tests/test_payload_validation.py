import pytest

from miso.api.base import ApiBase, ApiId


def null_func():
    pass


@pytest.mark.parametrize('api_id, payload', [
    (ApiId.BULK, {"data":[
        {"api_name":"search/search", "body": {"user_id": "usr", "q": "star", "fq":"title:love"}},
    ]}),
    (ApiId.EXPERIMENT_SEND, {"experiment": "a", "user_id": "usr"}),
    (ApiId.INTERACTION_UPLOAD, {"data": [{"user_id":"usr","type":"search"}]}),
    (ApiId.INTERACTION_DELETE, {}),
    (ApiId.PRODUCT_UPLOAD, {"data":[{}]}),
    (ApiId.PRODUCT_READ, {}),
    (ApiId.PRODUCT_DELETE, {}),
    (ApiId.QA_ANSWER, {"q": "what is love", "min_probability": 0}),
    (ApiId.QA_ANSWER, {"q": "what is love", "min_probability": 0.3}),
    (ApiId.QA_UPLOAD, {}),
    (ApiId.QA_AUTOCOMPLETE, {}),
    (ApiId.REC_U2I, {"user_id": "usr",}),
    (ApiId.REC_U2C, {"user_id": "usr",}),
    (ApiId.REC_U2A, {"user_id": "usr",}),
    (ApiId.REC_U2T, {"user_id": "usr",}),
    (ApiId.REC_I2I, {"user_id": "usr", "product_ids":["1", "2", "3"]}),
    (ApiId.SEARCH, {"user_id": "usr", "q": "star"}),
    (ApiId.AUTOCOMPLETE, {"user_id": "usr", "q": "aut"}),
    (ApiId.MGET, {"product_ids":["1", "2", "3"]}),
    (ApiId.USER_UPLOAD, {"data":[{}]}),
    (ApiId.USER_READ, {}),
    (ApiId.USER_DELETE, {}),
])
@pytest.mark.local
def test_validation_pass(api_id, payload):
    api_base = ApiBase(null_func)
    api_base.validate_payload(api_id, payload)


@pytest.mark.parametrize('api_id, payload', [
    (ApiId.BULK, {"data":{"api_name":"search/search", "body": {"user_id": "usr", "q": "star", "fq":"title:love"}}}),
    (ApiId.BULK, {"data":['star', 'trek', 'war', 'lord']}),
    (ApiId.EXPERIMENT_SEND, {"experiment": "a", "user_id": 123}),
    (ApiId.INTERACTION_UPLOAD, {"data": [1,2,3]}),
    (ApiId.INTERACTION_UPLOAD, {"data": {"user_id": "usr", "type": "search"}}),
    (ApiId.PRODUCT_UPLOAD, {"data":['1','2','3']}),
    (ApiId.PRODUCT_UPLOAD, {"data":{"id":"prod1", "title": "good product"}}),
    (ApiId.PRODUCT_READ, {"product_id": 123}),
    (ApiId.QA_ANSWER, {"q": ["what is love"], "min_probability": 0}),
    (ApiId.REC_I2I, {"user_id": "usr", "product_id":["1", "2", "3"]}),
    (ApiId.REC_I2I, {"user_id": "usr", "product_ids": "1,2,3"}),
    (ApiId.MGET, {"product_id":["1", "2", "3"]}),
    (ApiId.USER_UPLOAD, {"data":{}}),
])
@pytest.mark.local
def test_validation_fail(api_id, payload):
    api_base = ApiBase(null_func)
    with pytest.raises(ValueError, match=r".* shoud be .*"):
        api_base.validate_payload(api_id, payload)


@pytest.mark.parametrize('api_id, payload', [
    (ApiId.REC_U2I, {}),
    (ApiId.REC_U2C, {}),
    (ApiId.REC_U2A, {}),
    (ApiId.REC_U2T, {}),
    (ApiId.REC_I2I, {"product_ids":["1", "2", "3"]}),
    (ApiId.SEARCH, {"q": "star"}),
    (ApiId.AUTOCOMPLETE, {"q": "aut"}),
])
def test_validation_need_user(api_id, payload):
    api_base = ApiBase(null_func)
    with pytest.raises(ValueError, match="Either user_id or anonymous_id need to be present"):
        api_base.validate_payload(api_id, payload)
