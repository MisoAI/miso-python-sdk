from .base import ApiBase


class UserApi(ApiBase):
    def upload(self, payload: dict):
        return self._api_call('v1/users', payload)


    def read(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self._api_call(path, {}, method='GET')


    def delete(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self._api_call(path, {}, method='DELETE')
