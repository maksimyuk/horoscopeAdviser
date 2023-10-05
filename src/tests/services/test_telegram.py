import pytest
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.models.subscription import Subscription
from services.telegram import TelegramService
from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test__telegram_service__telegram_user__create_subscription__ok(async_db_session: AsyncSession):
    user = await UserFactory.create(session=async_db_session)

    await TelegramService(session=async_db_session).create_or_update_subscription(
        telegram_user_id=user.telegram_user_id,
        source="1001",
        sign="pisces",
    )

    query = select(func.count(Subscription.id)).filter_by(user_id=user.id)
    assert await async_db_session.scalar(query) == 1
