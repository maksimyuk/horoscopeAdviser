
from sqlalchemy import select

from .base import BaseDatabaseRepository
from db.models.user import User
from schemas.user import CreateUserSchema


class UserRepository(BaseDatabaseRepository):

    async def create(self, create_data: CreateUserSchema):
        user = User(**create_data.model_dump())

        self._session.add(user)
        await self._session.flush()

        return user

    async def get_user_by_id(self, user_id: int) -> User | None:
        query = select(User).filter_by(id=user_id)
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()

    async def get_user_by_telegram_user_id(self, telegram_user_id: int) -> User | None:
        query = select(User).filter_by(telegram_user_id=telegram_user_id)
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()
