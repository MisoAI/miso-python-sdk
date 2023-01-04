from typing import List, Optional
from .base import ApiBase, ApiId


class SearchApi(ApiBase):
    def search(
        self,
        *,
        q: str,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        fl: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        start: Optional[int] = None,
        rows: Optional[int] = None,
        **extras,
    ):

        payload = self.prepare_payload({
            'q': q,
            'user_id': user_id,
            'anonymous_id': anonymous_id,
            'fl': fl,
            'fq': fq,
            'boost_fq': boost_fq,
            'start': start,
            'rows': rows,
        }, extras, ApiId.SEARCH)
        return self._api_call('v1/search/search', payload)


    def autocomplete(
        self,
        *,
        q: str,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        completion_fields: Optional[List[str]] = None,
        fl: Optional[List[str]] = None,
        start: Optional[int] = None,
        rows: Optional[int] = None,
        **extras,
    ):
        payload = self.prepare_payload({
            'q': q,
            'user_id': user_id,
            'anonymous_id': anonymous_id,
            'completion_fields': completion_fields,
            'fl': fl,
            'start': start,
            'rows': rows,
        }, extras, ApiId.AUTOCOMPLETE)

        return self._api_call('v1/search/autocomplete', payload)


    def multi_get(
        self,
        *,
        product_ids: List[str],
        fl: Optional[List[str]] = None,
        **extras,
    ):
        payload = self.prepare_payload({
            'product_ids': product_ids,
            'fl': fl,
        }, extras, ApiId.MGET)
        return self._api_call('v1/search/mget', payload)
