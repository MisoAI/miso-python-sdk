from typing import List

from .base import ApiBase


class RecommendationApi(ApiBase):
    def user_to_products(self, payload: dict):
        return self._api_call('v1/recommendation/user_to_products', payload)


    def user_to_categories(self, payload: dict):
        return self._api_call('v1/recommendation/user_to_categories', payload)


    def user_to_attributes(self, payload: dict):
        return self._api_call('v1/recommendation/user_to_attributes', payload)


    def user_to_trending(self, payload: dict):
        return self._api_call('v1/recommendation/user_to_trending', payload)


    def product_to_products(self, payload: dict):
        return self._api_call('v1/recommendation/product_to_products', payload)
