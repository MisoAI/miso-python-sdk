from typing import Dict, List, Optional, Union
from .base import ApiBase, ApiId


class QAApi(ApiBase):
    def question_answering(
        self,
        *,
        q: str,
        min_probability: float,
        rows: Optional[int] = None,
        fl: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        **extras,
    ):
        payload = self.prepare_payload({
            "q": q,
            "min_probability": min_probability,
            "rows": rows,
            "fl": fl,
            "fq": fq,
            "boost_fq": boost_fq,
        }, extras, ApiId.QA_ANSWER)
        return self._api_call('v1/qa/question_answering', payload)


    def upload_question_bank(
        self,
        *,
        data: List[Dict[str, Union[str, float]]],
        **extras,
    ):
        payload = self.prepare_payload({
            "data": data,
        }, extras, ApiId.QA_UPLOAD)
        return self._api_call('v1/qa/questions', payload)


    def question_autocomplete(
        self,
        *,
        q: str,
        rows: Optional[int] = None,
        **extras,
    ):
        payload = self.prepare_payload({
            "q": q,
            "rows": rows,
        }, extras, ApiId.QA_AUTOCOMPLETE)
        return self._api_call('v1/qa/question_autocomplete', payload)
