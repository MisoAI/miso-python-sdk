from typing import Callable


class ApiBase:
    def __init__(
        self,
        call_func: Callable,
    ):
        self._api_call = call_func
