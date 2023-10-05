from sqlalchemy.ext.asyncio import AsyncSession

from db.enums import HoroscopeSigns, Sources
from db.models.subscription import Subscription
from db.repositories.subscription import SubscriptionRepository
from db.repositories.user import UserRepository
from schemas.subscription import SubscriptionCreateSchema, SubscriptionUpdateSchema


class SubscriptionService:
    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session
        self._user_repository = UserRepository(session)
        self._subscription_repository = SubscriptionRepository(session)

    async def set_default_subscription(
        self,
        telegram_user_id: int,
        sign: HoroscopeSigns,
        source: Sources,
    ) -> Subscription:
        user = await self._user_repository.get_or_create_by_telegram_user_id(telegram_user_id=telegram_user_id)

        current_subscription = await self._subscription_repository.get_by_user_id(user.id)
        if current_subscription:
            subscription_update_data = SubscriptionUpdateSchema(user_id=user.id, sign=sign, source=source)
            result = await self._subscription_repository.update_by_user_id(
                user_id=user.id,
                update_data=subscription_update_data,
            )
        else:
            subscription_create_data = SubscriptionCreateSchema(user_id=user.id, sign=sign, source=source)
            result = await self._subscription_repository.create(subscription_create_data)

        await self._session.commit()

        return result
