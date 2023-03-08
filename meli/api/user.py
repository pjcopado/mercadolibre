from meli.base import Client, api_endpoint, fill_query_params, ApiResponse


class User(Client):
    """ """

    @api_endpoint("/users/{}", method="GET")
    def get_by_id(self, user_id: str, **kwargs) -> ApiResponse:
        """
        get_user_by_id(self, user_id: str, **kwargs) -> ApiResponse
        Get user by id: User account information.

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
    def put_by_id(self, user_id: str, body: dict, **kwargs) -> ApiResponse:
        """
        put_user_by_id(self, user_id: str, body: dict, **kwargs) -> ApiResponse
        Put user by id: User account information.

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

    @api_endpoint("/users/me", method="GET")
    def get_logged_user_info(self, **kwargs) -> ApiResponse:
        """
        get_logged_user_info(self, **kwargs) -> ApiResponse
        Get User: Returns account information about the authenticated user.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_logged_user_info()

        Args:

            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path")), params=kwargs)

    @api_endpoint("/users/{}/addresses", method="GET")
    def get_addresses(self, user_id: str, **kwargs) -> ApiResponse:
        """
        get_user_addresses(self, user_id: str, **kwargs) -> ApiResponse
        User addresses: Returns payment methods accepted by a seller to collect its operations.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_user_addresses(user_id='XXXXX')

        Args:
            user_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), user_id), params=kwargs
        )

    @api_endpoint("/users/{}/accepted_payment_methods", method="GET")
    def get_accepted_payment_methods(self, user_id: str, **kwargs) -> ApiResponse:
        """
        get_accepted_payment_methods(self, user_id: str, **kwargs) -> ApiResponse
        Accepted payment methods: Returns payment methods accepted by a seller to collect its operations.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_accepted_payment_methods(user_id='XXXXX')

        Args:
            user_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), user_id), params=kwargs
        )

    @api_endpoint("/users/{}/brands", method="GET")  # TODO NO FUNCIONA
    def get_brands(self, user_id: str, **kwargs) -> ApiResponse:
        """
        get_brands(self, user_id: str, **kwargs) -> ApiResponse
        User brands: This resource retrieves brands associated to an user_id. The official_store_id attribute identifies a store.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_brands(user_id='XXXXX')

        Args:
            user_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), user_id), params=kwargs
        )
