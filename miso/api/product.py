from typing import Any, Dict, List
from .base import ApiBase


class ProductApi(ApiBase):
    def upload(self, *, data:List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({
            "data": data,
        }, extras)
        return self._api_call('v1/product', payload)


    def read(self, *, product_id: str, **extras):
        payload = self.prepare_payload({}, extras)
        path = f'v1/products/{product_id}'
        return self._api_call(path, payload, method='GET')


    def delete(self, *, product_id: str, **extras):
        payload = self.prepare_payload({}, extras)
        path = f'v1/products/{product_id}'
        return self._api_call(path, payload, method='DELETE')
