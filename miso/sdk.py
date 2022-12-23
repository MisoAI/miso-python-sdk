import requests

from .api.bulk import BulkApi
from .api.experiment import ExperimentApi
from .api.interaction import InteractionApi
from .api.product import ProductApi
from .api.qa import QAApi
from .api.recommendation import RecommendationApi
from .api.search import SearchApi
from .api.user import UserApi
from .version import SDK_VERSION


class ApiException(Exception):
    def __init__(self, message, status_code: int, response: dict):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class ApiClient:
    VERSION = SDK_VERSION

    def __init__(
        self,
        api_key: str,
        host: str = 'https://api.askmiso.com',
        raise_on_error: bool = False,
    ):
        session = requests.Session()

        session.params.update({
            'api_key': api_key,
        })

        session.headers.update({
            'User-Agent': f'miso-sdk-python/{self.VERSION}',
        })

        def api_call(
            path: str,
            payload: dict,
            method: str = 'POST'
        ):
            url = f'{host}/{path}'

            resp = session.request(method, url, json=payload)
            data = resp.json()

            status = resp.status_code
            if raise_on_error and status >= 400:
                msg = f"API requset failed, status = {status}, message = `{data.get('message')}`"
                raise ApiException(msg, resp.status_code, data)
            result = resp.json()

            # automatically unpack data for succesful requests
            if status == 200 and 'data' in result:
                result = result['data']

            return result

        self.interaction = InteractionApi(api_call)
        self.product = ProductApi(api_call)
        self.user = UserApi(api_call)
        self.search = SearchApi(api_call)
        self.recommendation = RecommendationApi(api_call)
        self.qa = QAApi(api_call)
        self.bulk = BulkApi(api_call)
        self.experiment = ExperimentApi(api_call)
