import datetime

from server.horoscopes.db.base import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, func


class User(Base):
    """User db schema."""

    time_created: datetime.datetime = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        doc="Date and time of creating user",
    )
    time_updated: datetime.datetime = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        doc="Date and time of updating user",
    )
    is_active: bool = Column(
        Boolean(),
        default=True,
        doc="sign is user currently active",
    )
    telegram_user_id: int = Column(
        Integer(),
        doc="ID of user inside telegram",
    )
