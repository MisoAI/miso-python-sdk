from enum import auto, Enum
from typing import Any, Callable, Dict


class ApiId(Enum):
    BULK = auto()
    EXPERIMENT_SEND = auto()
    INTERACTION_UPLOAD = auto()
    INTERACTION_DELETE = auto()
    PRODUCT_UPLOAD = auto()
    PRODUCT_READ = auto()
    PRODUCT_DELETE = auto()
    QA_ANSWER = auto()
    QA_UPLOAD = auto()
    QA_AUTOCOMPLETE = auto()
    REC_U2I = auto()
    REC_U2C = auto()
    REC_U2A = auto()
    REC_U2T = auto()
    REC_I2I = auto()
    SEARCH = auto()
    AUTOCOMPLETE = auto()
    MGET = auto()
    USER_UPLOAD = auto()
    USER_READ = auto()
    USER_DELETE = auto()

Number = (int, float)

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
        api_id: ApiId,
    ) -> Dict[str, Any]:
        none_keys = [k for k, v in inputs.items() if v is None]
        for key in none_keys:
            inputs.pop(key, None)

        inputs.update(extras)

        self.validate_payload(api_id, inputs)

        return inputs


    def validate_payload(self, api_id: ApiId, payload: Dict[str, Any]):
        errors = []

        check_user = {
            ApiId.REC_U2I,
            ApiId.REC_U2C,
            ApiId.REC_U2A,
            ApiId.REC_U2T,
            ApiId.REC_I2I,
            ApiId.SEARCH,
            ApiId.AUTOCOMPLETE,
        }
        if api_id in check_user:
            if 'user_id' not in payload and 'anonymous_id' not in payload:
                errors.append("Either user_id or anonymous_id need to be present")

        # basic type checking
        types = {
            str: {'user_id', 'anonymous_id', 'product_id', 'q', 'fq', 'boost_fq'},
            int: {'rows', 'start'},
            Number: {'min_probability', 'weight', 'duration', 'rating', 'revenue'},
        }
        list_str_fields = {'fl', 'user_ids', 'product_ids'}

        for field, val in payload.items():
            # built-in types
            for field_type, typed_fields in types.items():
                if field in typed_fields \
                   and not isinstance(val, field_type): # type: ignore[arg-type]
                    errors.append(f"`{field}` ({val}) shoud be {field_type}, not {type(val)}")
            # generic types
            if field in list_str_fields:
                if not isinstance(val, list) \
                   or not all(isinstance(v, str) for v in val):
                    errors.append(f"`{field}` ({val}) shoud be a list of string")

        # data list
        data_list_apis = {
            ApiId.BULK,
            ApiId.USER_UPLOAD,
            ApiId.PRODUCT_UPLOAD,
            ApiId.INTERACTION_UPLOAD,
        }
        if api_id in data_list_apis and 'data' in payload:
            data = payload['data']
            if not isinstance(data, list) \
               or not all(isinstance(v, dict) for v in data):
                errors.append(f"`data` ({data}) shoud be a list of dict")

        if len(errors) > 0:
            raise ValueError('; '.join(errors))
