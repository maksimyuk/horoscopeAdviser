from sqlalchemy import select, update

from db.models.subscription import Subscription
from db.repositories.base import BaseDatabaseRepository
from schemas.subscription import SubscriptionCreateSchema, SubscriptionUpdateSchema


class SubscriptionRepository(BaseDatabaseRepository):
    async def create(self, create_data: SubscriptionCreateSchema) -> Subscription:
        subscription = Subscription(**create_data.model_dump())

        self._session.add(subscription)
        await self._session.flush()

        return subscription

    async def is_exists_by_user_id(self, user_id: int) -> bool:
        query = select(Subscription).filter_by(id=user_id)
        query_result = await self._session.execute(query)

        return query_result.first()

    async def get_by_user_id(self, user_id: int) -> Subscription | None:
        query = select(Subscription).filter_by(user_id=user_id)
        query_result = await self._session.execute(query)
        return query_result.scalar_one_or_none()

    async def update_by_user_id(self, user_id: int, update_data: SubscriptionUpdateSchema) -> None:
        query = (
            update(Subscription)
            .where(Subscription.user_id == user_id)
            .values(**update_data.model_dump(exclude_unset=True))
        )
        await self._session.execute(query)
        await self._session.flush()
