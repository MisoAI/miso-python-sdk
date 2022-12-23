from .base import ApiBase


class SearchApi(ApiBase):
    def search(self, payload: dict):
        return self._api_call('v1/search/search', payload)


    def autocomplete(self, payload: dict):
        return self._api_call('v1/search/autocomplete', payload)


    def multi_get(self, payload: dict):
        return self._api_call('v1/search/mget', payload)
