from typing import Dict, List, Union
from .base import ApiBase


class BulkApi(ApiBase):
    def bulk(self, *, requests: List[Dict[str, Union[str, dict]]], **extras):
        payload = self.prepare_payload({
            "requests": requests,
        }, extras)
        return self._api_call('v1/bulk', payload)
