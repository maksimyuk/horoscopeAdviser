from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from server.settings.components.database import get_database_url

engine = create_engine(get_database_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)
