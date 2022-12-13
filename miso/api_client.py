from typing import List
import requests


class ApiException(Exception):
    def __init__(self, message, status_code: int, response: dict):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class ApiClient:
    VERSION = '0.0.0'

    def __init__(
        self,
        api_key: str,
        host: str = 'https://api.askmiso.com',
        raise_on_error: bool = False,
    ):
        self.host = host
        self._session = requests.Session()

        self._session.params.update({
            'api_key': api_key,
        })

        self._session.headers.update({
            'User-Agent': f'miso-sdk-python/{self.VERSION}',
        })

        self.raise_on_error = raise_on_error


    def __api_call(
        self,
        path: str,
        payload: dict,
        method: str = 'POST'
    ):
        url = f'{self.host}/{path}'

        resp = self._session.request(method, url, json=payload)
        data = resp.json()

        status = resp.status_code
        if self.raise_on_error and status >= 400:
            msg = f"API requset failed, status = {status}, message = `{data.get('message')}`"
            raise ApiException(msg, resp.status_code, data)
        return resp.json()


    def experiment_send(self, experiment_id_or_slug: str, payload: dict):
        path = f"v1/experiments/{experiment_id_or_slug}/events"
        return self.__api_call(path, payload)


    def interaction_upload(self, payload: dict):
        return self.__api_call('v1/interactions', payload)


    def interaction_delete(self, payload: dict):
        return self.__api_call('v1/interactions', payload, method='DELETE')


    def product_upload(self, payload: dict):
        return self.__api_call('v1/products', payload)


    def product_read(self, product_id: str):
        path = f'v1/products/{product_id}'
        return self.__api_call(path, {}, method='GET')


    def product_delete(self, product_id: str):
        path = f'v1/products/{product_id}'
        return self.__api_call(path, {}, method='DELETE')


    def user_upload(self, payload: dict):
        return self.__api_call('v1/users', payload)


    def user_read(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self.__api_call(path, {}, method='GET')


    def user_delete(self, user_id: str):
        path = f'v1/users/{user_id}'
        return self.__api_call(path, {}, method='DELETE')


    def search(self, payload: dict):
        return self.__api_call('v1/search/search', payload)


    def autocomplete(self, payload: dict):
        return self.__api_call('v1/search/autocomplete', payload)


    def multi_get(self, product_ids: List[str]):
        payload = {"product_ids": product_ids}
        return self.__api_call('v1/search/mget', payload)
