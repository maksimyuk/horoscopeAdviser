from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from server.settings.components.database import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)
