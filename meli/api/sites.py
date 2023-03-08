from meli.base import Client, api_endpoint, fill_query_params, ApiResponse


class Sites(Client):
    """ """

    @api_endpoint("/sites", method="GET")
    def get_all(self, **kwargs) -> ApiResponse:
        """
        get_all(self, , **kwargs) -> ApiResponse
        Country sites: Retrieves information about the sites where MercadoLibre runs.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_all()

        Args:

            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @api_endpoint("/site_domains/{}", method="GET")
    def get_site_domain_by_id(self, domain_id: str, **kwargs) -> ApiResponse:
        """
        get_site_domain_by_id(self, domain_id: str, **kwargs) -> ApiResponse
        Returns information about the site domain.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_site_domain_by_id(domain_id='mercadolibre.com.ar')

        Args:
            domain_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), domain_id), params=kwargs
        )

    @api_endpoint("/sites/{}/listing_types", method="GET")
    def get_site_listing_types(self, site_id: str, **kwargs) -> ApiResponse:
        """
        get_site_listing_types(self, site_id: str, **kwargs) -> ApiResponse
        Returns information about listing types.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_site_listing_types(site_id='mercadolibre.com.ar')

        Args:
            site_id: str
            **kwargs:

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), site_id), params=kwargs
        )

    @api_endpoint("/sites/{}/listing_prices", method="GET")
    def get_site_listing_prices(self, site_id: str, **kwargs) -> ApiResponse:
        """
        get_site_listing_prices(self, site_id: str, **kwargs) -> ApiResponse
        Listing prices: Returns the listing price for selling and buying in Mercado Libre.

        **Usage Plan:**

        # ======================================  ==============
        # Rate (requests per second)               Burst
        # ======================================  ==============
        # 1                                       1
        # ======================================  ==============

        # For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = User().get_site_listing_prices(site_id='mercadolibre.com.ar')

        Args:
            site_id: str
            **kwargs:
                query **price**:*integer*. Price parameter greater or equal than 0.

        Returns:
            # GetCatalogItemResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), site_id), params=kwargs
        )
