from server.horoscopes.db.session import session
from server.horoscopes.models.user import User


class UserManager:
    """Manager for User model."""

    def __init__(self):
        self.model = User

    def create(self, telegram_user_id: int) -> User:
        new_user = self.model(
            telegram_user_id=telegram_user_id,
        )
        session.add(new_user)
        session.commit()

        return new_user
