from typing import Optional
from .base import ApiBase, ApiId


class ExperimentApi(ApiBase):
    def send(
        self,
        *,
        experiment: str,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        variant_name: Optional[str] = None,
        timestamp: Optional[str] = None,
        **extras,
    ):
        payload = self.prepare_payload({
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "variant_name": variant_name,
            "timestamp": timestamp,
        }, extras, ApiId.EXPERIMENT_SEND)

        path = f"v1/experiments/{experiment}/events"
        return self._api_call(path, payload)
