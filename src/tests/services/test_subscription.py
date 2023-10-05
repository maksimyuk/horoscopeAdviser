import pytest
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from db.enums import HoroscopeSigns, Sources
from db.models.subscription import Subscription
from services.subscription import SubscriptionService
from tests.factories.subscription import SubscriptionFactory
from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test__subscription_service__telegram_user__create_subscription__ok(async_db_session: AsyncSession):
    user = await UserFactory.create(session=async_db_session)

    await SubscriptionService(
        session=async_db_session,
    ).set_default_subscription(
        telegram_user_id=user.telegram_user_id,
        sign=HoroscopeSigns.LEO,
        source=Sources.HORO_1001,
    )

    query = select(func.count(Subscription.id)).filter_by(user_id=user.id)
    assert await async_db_session.scalar(query) == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "from_source,to_source",
    [
        (Sources.HORO_1001, Sources.HORO_MAIL),
        (Sources.HORO_MAIL, Sources.HORO_1001),
    ],
)
async def test__subscription_service__telegram_user__update_subscription__source__ok(
    async_db_session: AsyncSession,
    from_source: Sources,
    to_source: Sources,
):
    user = await UserFactory.create(session=async_db_session)
    subscription = await SubscriptionFactory.create(
        session=async_db_session,
        source=from_source,
        user_id=user.id,
    )

    await SubscriptionService(
        session=async_db_session,
    ).set_default_subscription(
        telegram_user_id=subscription.user.telegram_user_id,
        source=to_source,
        sign=subscription.sign,
    )

    query = select(func.count(Subscription.id)).filter_by(user_id=subscription.user_id)
    assert await async_db_session.scalar(query) == 1
    query = select(Subscription).filter_by(user_id=subscription.user_id)
    query_result = await async_db_session.execute(query)
    subscription_from_db = query_result.scalar_one()
    assert subscription_from_db.source == to_source
