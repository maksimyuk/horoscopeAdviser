from random import randint

import pytest

from server.horoscopes.services import UserManager


@pytest.fixture(scope="function")
def user(temp_db_session, telegram_user_id: int = None):
    """Fixture for creating user instance."""
    user, *_ = UserManager().get_or_create(
        telegram_user_id=telegram_user_id or randint(1, 100),
        session=temp_db_session,
    )

    return user
