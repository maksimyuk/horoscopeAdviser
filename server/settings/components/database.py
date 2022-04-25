import os

from server.settings.components import config

CONFIG_SQLALCHEMY_DATABASE_URI = config("DATABASE_URI")


def get_database_url() -> str:
    """Returns URL for database."""
    database_uri = CONFIG_SQLALCHEMY_DATABASE_URI

    if os.environ.get("TESTING"):
        database_uri = "_".join([database_uri, "test"])

    return database_uri
