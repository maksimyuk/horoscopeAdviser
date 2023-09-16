from .base import BaseSchema


class CreateUserSchema(BaseSchema):
    telegram_user_id: int
