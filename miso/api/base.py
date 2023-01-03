from typing import Any, Callable, Dict


class ApiBase:
    def __init__(
        self,
        call_func: Callable,
    ):
        self._api_call = call_func


    def prepare_payload(
        self,
        inputs: Dict[str, Any],
        extras: Dict[str, Any],
    ) -> Dict[str, Any]:
        none_keys = [k for k, v in inputs.items() if v is None]
        for key in none_keys:
            inputs.pop(key, None)

        inputs.update(extras)
        return inputs
