from server.horoscopes.models.user import User
from server.horoscopes.services import UserManager


class TestUserManager:
    """Test-case for checking work of base operations with User-model."""

    def test_create_user(self, temp_db_session):
        # TODO change db data to rollback to every test
        assert temp_db_session.query(User).filter_by(telegram_user_id=2).count() == 0

        UserManager().get_or_create(telegram_user_id=2, session=temp_db_session)

        assert temp_db_session.query(User).filter_by(telegram_user_id=2).count() == 1
