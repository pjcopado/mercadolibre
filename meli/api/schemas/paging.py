from typing import Optional
from meli.api.schemas.common import OrmBaseModel


class Paging(OrmBaseModel):
    total: int
    offset: int
    limit: int
    primary_results: Optional[int]
