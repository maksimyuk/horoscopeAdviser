from sqlalchemy.ext.asyncio import AsyncSession

from db.enums import HoroscopeSigns
from db.session import get_async_session
from services.subscription import Sources, SubscriptionService


class TelegramService:
    def __init__(self, session: AsyncSession | None = None):
        session = session or get_async_session()()
        self._session = session
        self._subscription_service = SubscriptionService(session=session)

    async def create_or_update_subscription(
        self,
        telegram_user_id: int,
        sign: str,
        source: str,
    ):
        sign_as_enum = HoroscopeSigns.get_by_value(sign)
        source_as_enum = Sources.get_by_value(source)

        await self._subscription_service.set_default_subscription(
            telegram_user_id=telegram_user_id,
            sign=sign_as_enum,
            source=source_as_enum,
        )
