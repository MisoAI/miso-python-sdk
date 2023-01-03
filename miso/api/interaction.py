from typing import Any, Dict, List
from .base import ApiBase


class InteractionApi(ApiBase):
    def upload(self, *, data: List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({
            "data": data,
        }, extras)
        return self._api_call('v1/interactions', payload)


    def delete(self, *, user_ids: List[str], **extras):
        payload = self.prepare_payload({
            "user_ids": user_ids,
        }, extras)
        return self._api_call('v1/interactions', payload, method='DELETE')
