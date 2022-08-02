from sqlalchemy.orm import Session, joinedload

from server.horoscopes.base.sql_utils import try_flush_commit
from server.horoscopes.db.session import session as _session
from server.horoscopes.enums import (
    HoroscopeSigns,
    NotificationFrequency,
    Sources,
)
from server.horoscopes.models.subscription import Subscription
from server.horoscopes.models.user import User


class UserManager:
    """Manager for User model."""

    def __init__(self) -> None:
        self.model = User

    def get_instance(self, session: Session = _session, **kwargs) -> User | None:
        """Returns instance by given filters."""
        return session.query(self.model).filter_by(**kwargs).one_or_none()

    def get_or_create(
        self, session: Session = _session, commit: bool = True, **kwargs
    ) -> tuple[User | None, bool]:
        """Add new user to bot."""
        instance = self.get_instance(session=session, **kwargs)
        if instance:
            return instance, bool(instance)

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


class SubscriptionManager:
    """Manager for subscription model."""

    @classmethod
    def get_instance(cls, session: Session = _session, **kwargs) -> Subscription | None:
        """Returns instance of Subscription by given filters."""
        return (
            session.query(Subscription)
            .options(joinedload(Subscription.user))
            .filter_by(**kwargs)
            .one_or_none()
        )

    @classmethod
    def create(
        cls,
        user_id: int,
        notification_frequency: NotificationFrequency,
        sign: HoroscopeSigns,
        source: Sources,
        session: Session = _session,
        commit: bool = True,
    ) -> Subscription:
        """Creates instance of subscription with given params."""
        # TODO add check exists
        instance = Subscription(
            user_id=user_id,
            notification_frequency=notification_frequency,
            sign=sign,
            source=source,
        )
        try_flush_commit(session=session, commit=commit)

        return instance
