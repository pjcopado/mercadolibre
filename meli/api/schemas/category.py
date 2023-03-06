from datetime import datetime
from typing import Optional, List
from meli.api.schemas.common import OrmBaseModel
from meli.base.marketplaces import Currencies
from .status import Status


class CategoryShort(OrmBaseModel):
    id: str
    name: str


class CategoryChildren(CategoryShort):
    total_items_in_this_category: int


class Settings(OrmBaseModel):
    adult_content: bool
    buying_allowed: bool
    buying_modes: List[str]  # BuyingMode
    catalog_domain: str
    coverage_areas: str
    currencies: List[Currencies]
    fragile: bool
    immediate_payment: str
    item_conditions: List[str]  # ItemCondition
    items_reviews_allowed: bool
    listing_allowed: bool
    max_description_length: int
    max_pictures_per_item: int
    max_pictures_per_item_var: int
    max_sub_title_length: int
    max_title_length: int
    maximum_price: Optional[int]
    minimum_price: Optional[int]
    mirror_category: Optional[str]
    mirror_master_category: Optional[str]
    mirror_slave_categories: List[str]
    price: str
    reservation_allowed: str
    restrictions: List[str]
    rounded_address: bool
    seller_contact: str
    shipping_modes: List[str]
    shipping_options: List[str]
    shipping_profile: str
    show_contact_information: bool
    simple_shipping: str
    stock: str
    sub_vertical: str
    subscribable: bool
    tags: List[str]
    vertical: str
    vip_subdomain: str
    buyer_protection_programs: Optional[str]
    status: Status


class Category(OrmBaseModel):
    id: str
    name: str
    picture: Optional[str]
    permalink: Optional[str]
    total_items_in_this_category: int
    path_from_root: List[CategoryShort]
    children_categories: List[CategoryChildren]
    attribute_types: str
    settings: Settings
    meta_categ_id: Optional[str]
    attributable: bool
    date_created: datetime
