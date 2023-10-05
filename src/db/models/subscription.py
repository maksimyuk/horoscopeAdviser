from sqlalchemy import Boolean, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.enums import HoroscopeSigns, Sources

from .base import BaseModel
from .user import User


class Subscription(BaseModel):
    """User's Subscription to notification sb schema."""

    __table_args__ = (UniqueConstraint("user_id", "sign", "source"),)

    active: Mapped[bool] = mapped_column(
        Boolean(),
        doc="Is subscription active",
        default=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        doc="Reference to telegram-user model",
    )
    sign: Mapped[HoroscopeSigns] = mapped_column(
        Enum(HoroscopeSigns),
        doc="Sign of horoscope subscription for",
    )
    source: Mapped[Sources] = mapped_column(
        Enum(Sources),
        doc="Source of horoscope subscription",
    )

    user: Mapped[User] = relationship(  # type: ignore
        "User",
        back_populates="subscription",
        foreign_keys="Subscription.user_id",
    )
