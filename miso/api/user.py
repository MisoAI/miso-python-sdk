from typing import Any, Dict, List
from .base import ApiBase, ApiId


class UserApi(ApiBase):
    def upload(self, data: List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({"data": data}, extras, ApiId.USER_UPLOAD)
        return self._api_call('v1/users', payload)


    def read(self, user_id: str, **extras):
        payload = self.prepare_payload({}, extras, ApiId.USER_READ)
        path = f'v1/users/{user_id}'
        return self._api_call(path, payload, method='GET')


    def delete(self, user_id: str, **extras):
        payload = self.prepare_payload({}, extras, ApiId.USER_DELETE)
        path = f'v1/users/{user_id}'
        return self._api_call(path, payload, method='DELETE')
