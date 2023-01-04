from typing import Any, Dict, List
from .base import ApiBase, ApiId


class InteractionApi(ApiBase):
    def upload(self, *, data: List[Dict[str, Any]], **extras):
        payload = self.prepare_payload({
            "data": data,
        }, extras, ApiId.INTERACTION_UPLOAD)
        return self._api_call('v1/interactions', payload)


    def delete(self, *, user_ids: List[str], **extras):
        payload = self.prepare_payload({
            "user_ids": user_ids,
        }, extras, ApiId.INTERACTION_DELETE)
        return self._api_call('v1/interactions', payload, method='DELETE')
