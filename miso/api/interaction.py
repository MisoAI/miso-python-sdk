from .base import ApiBase


class InteractionApi(ApiBase):
    def upload(self, payload: dict):
        return self._api_call('v1/interactions', payload)


    def delete(self, payload: dict):
        return self._api_call('v1/interactions', payload, method='DELETE')
