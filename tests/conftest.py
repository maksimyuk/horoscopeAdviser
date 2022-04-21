from typing import Generator

import pytest
from server.horoscopes.db.session import SessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    """Get SQLAlchemy session."""
    yield SessionLocal()
