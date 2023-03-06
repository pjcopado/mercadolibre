from typing import Optional, List
from datetime import datetime
from meli.api.schemas.common import OrmBaseModel


class Address(OrmBaseModel):
    state: Optional[str]
    city: Optional[str]


class Ratings(OrmBaseModel):
    negative: int
    neutral: int
    positive: int


class Transactions(OrmBaseModel):
    canceled: int
    completed: int
    period: str
    ratings: Optional[dict]
    total: int


class SellerReputation(OrmBaseModel):
    level_id: Optional[str]
    power_seller_status: Optional[str]
    transactions: Transactions


class BuyerReputation(OrmBaseModel):
    tags: List[str]


class Status(OrmBaseModel):
    site_status: List[str]


class User(OrmBaseModel):
    id: int
    nickname: str
    registration_date: datetime
    country_id: str
    address: Address
    user_type: str
    tags: List[str]
    logo: Optional[str]
    points: int
    site_id: str
    permalink: str
    seller_reputation: SellerReputation
    buyer_reputation: BuyerReputation
    status: Status
