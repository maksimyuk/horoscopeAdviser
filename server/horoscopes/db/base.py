
# Import all the models, so that Base has them before being
# imported by Alembic
from server.horoscopes.db.base_class import Base  # noqa: F401
from server.horoscopes.models.user import User  # noqa: F401
