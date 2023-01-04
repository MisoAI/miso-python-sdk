from typing import List, Optional
from .base import ApiBase, ApiId


class RecommendationApi(ApiBase):
    def user_to_products(
        self,
        *,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        rows: Optional[int] = None,
        type: Optional[str] = None,
        fl: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        pagination_id: Optional[str] = None,
        start: Optional[int] = None,
        **extras
    ):
        payload = self.prepare_payload({
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "rows": rows,
            "type": type,
            "fl": fl,
            "fq": fq,
            "boost_fq": boost_fq,
            "pagination_id": pagination_id,
            "start": start,
        }, extras, ApiId.REC_U2I)
        return self._api_call('v1/recommendation/user_to_products', payload)


    def user_to_categories(
        self,
        *,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        rows: Optional[int] = None,
        type: Optional[str] = None,
        fl: Optional[List[str]] = None,
        products_per_category: Optional[int] = None,
        root_category: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        **extras
    ):
        payload = self.prepare_payload({
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "rows": rows,
            "type": type,
            "fl": fl,
            "products_per_category": products_per_category,
            "root_category": root_category,
            "fq": fq,
            "boost_fq": boost_fq,
        }, extras, ApiId.REC_U2C)
        return self._api_call('v1/recommendation/user_to_categories', payload)


    def user_to_attributes(
        self,
        *,
        field: str,
        boost_attributes: Optional[List[str]] = None,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        rows: Optional[int] = None,
        type: Optional[str] = None,
        fl: Optional[List[str]] = None,
        products_per_attribute: Optional[int] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        **extras
    ):
        payload = self.prepare_payload({
            "field": field,
            "boost_attributes": boost_attributes,
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "rows": rows,
            "type": type,
            "fl": fl,
            "products_per_attribute": products_per_attribute,
            "fq": fq,
            "boost_fq": boost_fq,
        }, extras, ApiId.REC_U2A)
        return self._api_call('v1/recommendation/user_to_attributes', payload)


    def user_to_trending(
        self,
        *,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        rows: Optional[int] = None,
        type: Optional[str] = None,
        fl: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        pagination_id: Optional[str] = None,
        start: Optional[int] = None,
        **extras
    ):
        payload = self.prepare_payload({
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "rows": rows,
            "type": type,
            "fl": fl,
            "fq": fq,
            "boost_fq": boost_fq,
            "pagination_id": pagination_id,
            "start": start,
        }, extras, ApiId.REC_U2T)
        return self._api_call('v1/recommendation/user_to_trending', payload)


    def product_to_products(
        self,
        *,
        user_id: Optional[str] = None,
        anonymous_id: Optional[str] = None,
        rows: Optional[int] = None,
        type: Optional[str] = None,
        fl: Optional[List[str]] = None,
        product_id: Optional[str] = None,
        product_ids: Optional[List[str]] = None,
        product_group_id: Optional[str] = None,
        product_group_ids: Optional[List[str]] = None,
        fq: Optional[str] = None,
        boost_fq: Optional[str] = None,
        pagination_id: Optional[str] = None,
        start: Optional[int] = None,
        **extras
    ):
        payload = self.prepare_payload({
            "user_id": user_id,
            "anonymous_id": anonymous_id,
            "rows": rows,
            "type": type,
            "fl": fl,
            "product_id": product_id,
            "product_ids": product_ids,
            "product_group_id": product_group_id,
            "product_group_ids": product_group_ids,
            "fq": fq,
            "boost_fq": boost_fq,
            "pagination_id": pagination_id,
            "start": start,
        }, extras, ApiId.REC_I2I)
        return self._api_call('v1/recommendation/product_to_products', payload)
