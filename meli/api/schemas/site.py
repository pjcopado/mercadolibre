from meli.api.schemas.common import OrmBaseModel
from meli.base.marketplaces import Currencies, MarketplacesIds


class Site(OrmBaseModel):
    default_currency_id: Currencies
    id: MarketplacesIds
    name: str
