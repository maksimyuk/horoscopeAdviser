import datetime

from server.horoscopes.db.base import Base
from sqlalchemy import Column, DateTime, Integer, func


class User(Base):
    """User db schema."""

    time_created: datetime.datetime = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        doc="Date and time of creating user",
    )
    telegram_user_id: int = Column(
        Integer(),
        doc="ID of user inside telegram",
    )
