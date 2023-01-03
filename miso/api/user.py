from typing import Any, Dict, List
from .base import ApiBase


class UserApi(ApiBase):
    def upload(self, data: List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({"data": data}, extras)
        return self._api_call('v1/users', payload)


    def read(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self._api_call(path, {}, method='GET')


    def delete(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self._api_call(path, {}, method='DELETE')
