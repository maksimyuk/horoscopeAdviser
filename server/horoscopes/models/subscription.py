from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey

from server.horoscopes.db.base import Base  # type: ignore
from server.horoscopes.enums import HoroscopeSigns, NotificationFrequency


class HoroscopeSubscription(Base):
    """User's Subscription to notification sb schema."""

    active: bool = Column(
        Boolean(),
        doc="Is subscription active",
        default=True,
    )

    user_id: int = Column(
        ForeignKey("horoscopes.models.user.User", ondelete="CASCADE"),
        doc="Reference to telegram-user model",
    )

    notification_frequency = Column(
        Enum(NotificationFrequency),
        doc="Frequency of notification to send to user",
    )

    # TODO fix field type to time only
    notification_datetime = Column(
        DateTime(timezone=True),
        doc="Date and time of sending notification",
    )

    horoscope_sign = Column(
        Enum(HoroscopeSigns),
        doc="Sign of horoscope subscription for",
    )

    #  TODO add field type of horoscope source
