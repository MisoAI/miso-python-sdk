class ApiBase:
    def __init__(
        self,
        call_func: callable,
    ):
        self._api_call = call_func
