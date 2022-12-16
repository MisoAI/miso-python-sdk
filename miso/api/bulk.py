from .base import ApiBase


class BulkApi(ApiBase):
    def bulk(self, payload: dict):
        return self._api_call('v1/bulk', payload)
