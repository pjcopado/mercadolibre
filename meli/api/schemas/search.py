from typing import List
from meli.api.schemas.common import OrmBaseModel
from meli.base.marketplaces import MarketplacesIds
from .paging import Paging
from .product import Product


class Search(OrmBaseModel):
    site_id: MarketplacesIds
    query: str
    paging: Paging
    results: List[Product]
