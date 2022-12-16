from .base import ApiBase


class ProductApi(ApiBase):
    def upload(self, payload: dict):
        return self._api_call('v1/product', payload)


    def read(self, product_id: str):
        path = f'v1/products/{product_id}'
        return self._api_call(path, {}, method='GET')


    def delete(self, product_id: str):
        path = f'v1/products/{product_id}'
        return self._api_call('v1/product', {}, method='DELETE')
