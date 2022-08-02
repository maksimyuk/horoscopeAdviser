from sqlalchemy import Boolean, Column, Enum, ForeignKey, Time

from server.horoscopes.db.base import Base
from server.horoscopes.enums import (
    HoroscopeSigns,
    NotificationFrequency,
    Sources,
)


class Subscription(Base):
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
    notification_datetime = Column(
        Time(timezone=True),
        doc="Date and time of sending notification",
    )
    sign = Column(
        Enum(HoroscopeSigns),
        doc="Sign of horoscope subscription for",
    )
    source = Column(
        Enum(Sources),
        doc="Source of horoscope subscription",
    )
