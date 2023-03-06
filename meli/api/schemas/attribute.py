from datetime import datetime
from typing import Optional, List, Dict, Any
from meli.api.schemas.common import OrmBaseModel
from meli.base.marketplaces import Currencies


class Tag(OrmBaseModel):
    catalog_required: Optional[bool]
    hidden: Optional[bool]
    multivalued: Optional[bool]
    variation_attribute: Optional[bool]
    used_hidden: Optional[bool]
    validate: Optional[bool]
    read_only: Optional[bool]


class Unit(OrmBaseModel):
    id: str
    name: str


class Value(OrmBaseModel):
    id: str
    name: str
    struct: Optional[Dict[str, Any]]
    source: Optional[int]


class Attribute(OrmBaseModel):
    id: str
    name: str
    tags: Optional[Tag]
    hierarchy: Optional[str]
    relevance: Optional[int]
    type: Optional[str]
    value_type: Optional[str]
    value_id: Optional[str]
    value_name: Optional[str]
    value_struct: Optional[str]
    values: Optional[Any]
    value_max_length: int
    allowed_units: Optional[List[Unit]]
    default_unit: Optional[str]
    tooltip: Optional[str]
    attribute_group_id: str
    attribute_group_name: str
    hint: Optional[str]
