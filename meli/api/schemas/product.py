from datetime import datetime
from typing import Optional, List, Any
from meli.base.marketplaces import Currencies, MarketplacesIds
from .common import OrmBaseModel
from .attribute import Attribute
from .status import Status


class Picture(OrmBaseModel):
    id: str
    url: str
    secure_url: str
    size: str
    max_size: str
    quality: str


class Description(OrmBaseModel):
    pass


class NonMercadoPagoPaymentMethods(OrmBaseModel):
    pass


class Shipping(OrmBaseModel):
    mode: str
    methods: List[str]
    tags: List[str]
    dimensions: Optional[str]
    local_pick_up: bool
    free_shipping: bool
    logistic_type: str
    store_pick_up: bool


class SellerAddress(OrmBaseModel):
    id: int


class Location(OrmBaseModel):
    pass


class CoverageAeas(OrmBaseModel):
    pass


class Variation(OrmBaseModel):
    id: int
    price: float
    attribute_combinations: List[Attribute]
    available_quantity: int
    sold_quantity: int
    sale_terms: List[str]
    picture_ids: List[str]
    catalog_product_id: Optional[str]


class ProductBase(OrmBaseModel):
    site_id: MarketplacesIds
    title: str
    subtitle: Optional[str]
    seller_id: int
    category_id: str
    official_store_id: Optional[int]
    price: int
    base_price: int
    original_price: Optional[int]
    currency_id: Currencies
    initial_quantity: int
    available_quantity: int
    sold_quantity: int
    sale_terms: List[str]
    buying_mode: str  # BuyingMode
    listing_type_id: str
    start_time: datetime
    historical_start_time: datetime
    stop_time: datetime
    condition: str  # Condition
    permalink: str
    thumbnail_id: str
    thumbnail: str
    secure_thumbnail: str
    pictures: List[Picture]
    video_id: Optional[str]
    descriptions: List[Description]
    accepts_mercadopago: bool
    non_mercado_pago_payment_methods: List[NonMercadoPagoPaymentMethods]
    shipping: Shipping
    international_delivery_mode: str
    seller_address: SellerAddress
    seller_contact: Optional[str]
    location: Location
    coverage_areas: CoverageAeas
    attributes: List[Attribute]
    warnings: List[Any]
    listing_source: str
    variations: List[Variation]
    status: Status
    sub_status: List[Any]
    tags: List[str]
    warranty: Optional[str]
    catalog_product_id: Optional[str]
    domain_id: str
    parent_item_id: Optional[str]
    differential_pricing: Optional[str]
    deal_ids: List[str]
    automatic_relist: bool
    date_created: datetime
    date_updated: datetime
    total_listing_fee: Optional[str]
    health: float
    catalog_listing: bool
    channels: List[str]
    bundle: Optional[str]


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: str
