from server.horoscopes.models.user import User
from server.horoscopes.services import UserManager


class TestUserManager:
    """Test-case for checking work of base operations with User-model."""

    def test_create_user(self, db):
        assert db.query(User).count() == 0

        UserManager().create(telegram_user_id=1)

        assert db.query(User).count() == 1
