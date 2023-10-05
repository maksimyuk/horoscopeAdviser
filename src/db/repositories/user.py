from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from core.exceptions.user import UserAlreadyExistsException
from db.models.user import User
from schemas.user import CreateUserSchema

from .base import BaseDatabaseRepository


class UserRepository(BaseDatabaseRepository):
    async def create(self, create_data: CreateUserSchema) -> User:
        user = User(**create_data.model_dump())

        self._session.add(user)

        try:
            await self._session.flush()
        except IntegrityError:
            raise UserAlreadyExistsException()

        return user

    async def get_by_id(self, user_id: int) -> User | None:
        query = select(User).filter_by(id=user_id)
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()

    async def get_by_telegram_user_id(self, telegram_user_id: int) -> User | None:
        query = select(User).filter_by(telegram_user_id=telegram_user_id)
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()

    async def get_or_create_by_telegram_user_id(self, telegram_user_id: int) -> User | None:
        user = await self.get_by_telegram_user_id(telegram_user_id)
        if not user:
            create_data = CreateUserSchema(telegram_user_id=telegram_user_id)
            user = await self.create(create_data)

        return user
