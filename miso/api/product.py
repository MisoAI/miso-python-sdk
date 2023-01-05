from typing import Any, Dict, List
from .base import ApiBase, ApiId


class ProductApi(ApiBase):
    def upload(self, *, data:List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({
            "data": data,
        }, extras, ApiId.PRODUCT_UPLOAD)
        return self._api_call('v1/products', payload)


    def read(self, *, product_id: str, **extras):
        payload = self.prepare_payload({}, extras, ApiId.PRODUCT_READ)
        path = f'v1/products/{product_id}'
        return self._api_call(path, payload, method='GET')


    def delete(self, *, product_id: str, **extras):
        payload = self.prepare_payload({}, extras, ApiId.PRODUCT_DELETE)
        path = f'v1/products/{product_id}'
        return self._api_call(path, payload, method='DELETE')
