import random

from server.horoscopes.enums import (
    HoroscopeSigns,
    NotificationFrequency,
    Sources,
)
from server.horoscopes.models.subscription import Subscription
from server.horoscopes.services import SubscriptionManager


class TestSubscriptionManager:
    """Test-case for checking work of manager with Subscription-model."""

    def test_create_subscription(self, temp_db_session, user):
        """Check new subscription is added."""
        assert temp_db_session.query(Subscription).count() == 0

        SubscriptionManager.create(
            session=temp_db_session,
            user_id=user.id,
            notification_frequency=random.choice(list(NotificationFrequency)),
            sign=random.choice(list(HoroscopeSigns)),
            source=random.choice(list(Sources)),
        )

        assert temp_db_session.query(Subscription).count() == 1
