import urllib.parse

from meli.base import Client, api_endpoint, fill_query_params, ApiResponse


class User(Client):
    """ """

    @api_endpoint("/users/{}")
    def get_user_by_id(self, user_id: str, **kwargs) -> ApiResponse:
        """
        get_user_by_id(self, user_id: str, **kwargs) -> ApiResponse
        Información de la cuenta del usuario.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_user_by_id(user_id='XXXXX')

        Args:
            user_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), user_id), params=kwargs
        )

    @api_endpoint("/users/{}", method="PUT")
    def put_user_by_id(self, user_id: str, body: dict, **kwargs) -> ApiResponse:
        """
        put_user_by_id(self, user_id: str, body: dict, **kwargs) -> ApiResponse
        Actualización de la información de la cuenta del usuario.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_user_by_id(user_id='XXXXX', body={})

        Args:
            user_id: str
            body: {}
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), user_id), params=kwargs, data=body
        )
