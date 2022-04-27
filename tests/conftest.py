import os

import alembic
import pytest
from alembic.config import Config
from server.settings.components.database import get_database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists, drop_database


@pytest.fixture(scope="session")
def set_test_environment():
    """Fixture for setting env to testing."""
    os.environ["TESTING"] = "1"


@pytest.fixture(scope="session")
def temp_db(set_test_environment):
    """Fixture for generating test db URL."""
    tmp_db_url = get_database_url()

    if database_exists(tmp_db_url):
        drop_database(tmp_db_url)

    create_database(tmp_db_url)

    try:
        yield tmp_db_url
    finally:
        drop_database(tmp_db_url)


@pytest.fixture(scope="session")
def temp_db_engine(temp_db):
    """Fixture for generating test db engine."""
    engine = create_engine(temp_db, echo=True)
    try:
        yield engine
    finally:
        engine.dispose()


@pytest.fixture(scope="session")
def apply_migrations(temp_db):
    """Apply migrations at beginning and end of testing session"""
    # https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest#about-testing
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield


@pytest.fixture()
def temp_db_session(temp_db_engine, apply_migrations):
    """Fixture for generating test db session."""
    yield Session(temp_db_engine)
