from .base import ApiBase


class QAApi(ApiBase):
    def question_answering(self, payload: dict):
        return self._api_call('v1/qa/question_answering', payload)


    def upload_question_bank(self, payload: dict):
        return self._api_call('v1/qa/questions', payload)


    def question_autocomplete(self, payload: dict):
        return self._api_call('v1/qa/question_autocomplete', payload)
