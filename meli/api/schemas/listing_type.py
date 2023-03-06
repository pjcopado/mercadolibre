from typing import Optional, List
from meli.api.schemas.common import OrmBaseModel
from meli.base.marketplaces import MarketplacesIds, Currencies


class ListingTypeShort(OrmBaseModel):
    site_id: MarketplacesIds
    id: str
    name: str


class DurationDays(OrmBaseModel):
    buy_it_now: int
    auction: Optional[str]
    classified: Optional[str]


class FeeCriteria(OrmBaseModel):
    min_fee_amount: bool
    max_fee_amount: bool
    percentage_of_fee_amount: int
    currency: Currencies


class Configuration(OrmBaseModel):
    name: str
    listing_exposure: str
    requires_picture: bool
    max_stock_per_item: int
    deduction_profile_id: Optional[str]
    differential_pricing_id: Optional[str]
    duration_days: DurationDays
    immediate_payment: DurationDays
    mercado_pago: str
    listing_fee_criteria: FeeCriteria
    sale_fee_criteria: FeeCriteria


class ListingType(OrmBaseModel):
    id: str
    not_available_in_categories: List[str]
    configuration: Configuration
    exceptions_by_category: List[str]
