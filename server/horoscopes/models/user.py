import datetime

from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.orm import relationship

from server.horoscopes.db.base import Base  # type: ignore


class User(Base):
    """User db schema."""

    __tablename__ = "users"

    time_created: datetime.datetime = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        doc="Date and time of creating user",
    )
    # TODO add unique
    telegram_user_id: int = Column(
        Integer(),
        doc="ID of user inside telegram",
    )

    subscription = relationship("Subscription", back_populates="user")
