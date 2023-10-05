"""Added subscription and user model

Revision ID: c034da489b9a
Revises:
Create Date: 2023-09-16 12:22:48.122059

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c034da489b9a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column(
            "time_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("telegram_user_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("users_pkey")),
    )
    op.create_index(op.f("users_id_idx"), "users", ["id"], unique=False)
    op.create_table(
        "subscriptions",
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "sign",
            sa.Enum(
                "ARIES",
                "TAURUS",
                "GEMINI",
                "CANCER",
                "LEO",
                "VIRGO",
                "LIBRA",
                "SCORPIO",
                "SAGITTARIUS",
                "CAPRICORN",
                "AQUARIUS",
                "PISCES",
                name="horoscopesigns",
            ),
            nullable=False,
        ),
        sa.Column(
            "source",
            sa.Enum("HORO_1001", "HORO_MAIL", name="sources"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("subscriptions_user_id_fkey"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("subscriptions_pkey")),
        sa.UniqueConstraint("user_id", "sign", "source", name=op.f("subscriptions_user_id_key")),
    )
    op.create_index(op.f("subscriptions_id_idx"), "subscriptions", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("subscriptions_id_idx"), table_name="subscriptions")
    op.drop_table("subscriptions")
    op.drop_index(op.f("users_id_idx"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###