from server.settings.components import config

SQLALCHEMY_DATABASE_URI = config("DATABASE_URI")
