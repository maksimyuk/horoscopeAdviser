import pytest

from server.horoscopes.models.user import User
from server.horoscopes.services import UserManager


class TestUserManager:
    """Test-case for checking work of base operations with User-model."""

    @pytest.mark.parametrize("telegram_user_id,users_count", [(1, 1)])
    def test_create_user(
        self, temp_db_session, telegram_user_id: int, users_count: int
    ):
        assert (
            temp_db_session.query(User)
            .filter_by(telegram_user_id=telegram_user_id)
            .count()
            == 0
        )

        UserManager().get_or_create(
            telegram_user_id=telegram_user_id, session=temp_db_session
        )

        assert (
            temp_db_session.query(User)
            .filter_by(telegram_user_id=telegram_user_id)
            .count()
            == users_count
        )
