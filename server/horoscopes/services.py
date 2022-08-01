from sqlalchemy.orm import Session

from server.horoscopes.base.sql_utils import try_flush_commit
from server.horoscopes.db.session import session as _session
from server.horoscopes.models.user import User


class UserManager:
    """Manager for User model."""

    def __init__(self) -> None:
        self.model = User

    def get_instance(self, session: Session = _session, **kwargs) -> User | None:
        """Returns instance by given filters."""
        return session.query(self.model).filter_by(**kwargs).one_or_none()

    def create(
        self, session: Session = _session, commit: bool = True, **kwargs
    ) -> tuple[User | None, bool]:
        """Add new user to bot."""
        instance = self.get_instance(session=session, **kwargs)
        if instance:
            return instance, False

        instance = self.model(**kwargs)
        session.add(instance)

        try_flush_commit(session=session, commit=commit)

        return instance, True

    def remove(
        self, session: Session = _session, commit: bool = True, **kwargs
    ) -> bool:
        """Remove user from bot."""
        instance = self.get_instance(session=session, **kwargs)
        if not instance:
            return False

        session.delete(instance)
        try_flush_commit(session=session, commit=commit)

        return True
