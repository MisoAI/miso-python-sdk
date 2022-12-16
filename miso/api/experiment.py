from .base import ApiBase


class ExperimentApi(ApiBase):
    def send(self, experiment_id_or_slug: str, payload: dict):
        path = f"v1/experiments/{experiment_id_or_slug}/events"
        return self._api_call(path, payload)
