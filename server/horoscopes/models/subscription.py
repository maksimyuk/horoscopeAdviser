from sqlalchemy import Boolean, Column, Enum, ForeignKey, Time, UniqueConstraint
from sqlalchemy.orm import relationship

from server.horoscopes.db.base import Base
from server.horoscopes.enums import (
    HoroscopeSigns,
    NotificationFrequency,
    Sources,
)


class Subscription(Base):
    """User's Subscription to notification sb schema."""

    __tablename__ = "subscription"
    __table_args__ = (
        UniqueConstraint("user_id", "notification_frequency", "sign", "source"),
    )

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

    # TODO add UNIQUE for user_id, notification_frequency, sign, source
