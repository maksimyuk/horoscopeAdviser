"""Added subscription table

Revision ID: 49bcae845342
Revises: 6038c550e8e9
Create Date: 2022-08-02 19:38:02.138302

"""
from alembic import op
import sqlalchemy as sa

from server.horoscopes.enums import HoroscopeSigns, NotificationFrequency, Sources

# revision identifiers, used by Alembic.
revision = "49bcae845342"
down_revision = "6038c550e8e9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "subscription",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("active", sa.BOOLEAN(), doc="Is subscription active", default=True),
        sa.Column("user_id", sa.INTEGER(), doc="Reference to telegram-user model"),
        sa.Column(
            "notification_frequency",
            sa.Enum(NotificationFrequency),
            doc="Frequency of notification to send to user",
        ),
        sa.Column(
            "notification_datetime",
            sa.TIME(timezone=True),
            doc="Date and time of sending notification",
        ),
        sa.Column(
            "sign", sa.Enum(HoroscopeSigns), doc="Sign of horoscope subscription for"
        ),
        sa.Column("source", sa.Enum(Sources), doc="Source of horoscope subscription"),
        sa.PrimaryKeyConstraint("id", name="subscription_pk"),
    )
    op.create_foreign_key(
        constraint_name="fk_subscription_user_id",
        source_table="subscription",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_table("subscription")
