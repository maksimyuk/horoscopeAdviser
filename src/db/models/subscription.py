from sqlalchemy import Boolean, Column, Enum, ForeignKey, Time, UniqueConstraint
from sqlalchemy.orm import relationship

from db.enums import HoroscopeSigns, NotificationFrequency, Sources

from .base import BaseModel


class Subscription(BaseModel):
    """User's Subscription to notification sb schema."""

    __table_args__ = (UniqueConstraint("user_id", "notification_frequency", "sign", "source"),)

    active: bool = Column(
        Boolean(),
        doc="Is subscription active",
        default=True,
    )
    user_id: int = Column(
        ForeignKey("users.id", ondelete="CASCADE"),
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

    user = relationship("User", back_populates="subscription")
