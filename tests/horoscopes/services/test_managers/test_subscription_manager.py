import random

from server.horoscopes.enums import (
    HoroscopeSigns,
    NotificationFrequency,
    Sources,
)
from server.horoscopes.models.subscription import Subscription
from server.horoscopes.services import SubscriptionManager, UserManager


class TestSubscriptionManager:
    """Test-case for checking work of manager with Subscription-model."""

    def test_create_subscription(self, temp_db_session):
        """Check new subscription is added."""
        assert temp_db_session.query(Subscription).count() == 0

        user, *_ = UserManager().get_or_create(
            telegram_user_id=1,
            session=temp_db_session,
        )

        SubscriptionManager.create(
            session=temp_db_session,
            user_id=user.id,
            notification_frequency=random.choice(list(NotificationFrequency)),
            sign=random.choice(list(HoroscopeSigns)),
            source=random.choice(list(Sources)),
        )

        assert temp_db_session.query(Subscription).count() == 1
