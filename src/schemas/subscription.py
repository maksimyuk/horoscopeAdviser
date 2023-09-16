from typing import Optional

from db.enums import HoroscopeSigns, Sources

from .base import BaseSchema


class SubscriptionCreateSchema(BaseSchema):
    user_id: int
    sign: HoroscopeSigns
    source: Sources
    active: bool = True


class SubscriptionUpdateSchema(BaseSchema):
    user_id: int
    sign: Optional[HoroscopeSigns] = None
    source: Optional[Sources] = None
    active: Optional[bool] = None


class SubscriptionCreateOrUpdateSchema(SubscriptionUpdateSchema):
    pass
