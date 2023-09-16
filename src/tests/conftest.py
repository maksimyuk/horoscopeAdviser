import asyncio
import os
import typing

import alembic.command
import pytest
import pytest_asyncio
from alembic.config import Config
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy_utils import create_database, database_exists, drop_database

from core.config import settings
from db.session import get_engine

pytestmark = pytest.mark.asyncio


@pytest.fixture(scope="session")
def test_environment():
    settings.cache_clear()
    os.environ["TESTING"] = "1"


@pytest.fixture(scope="session")
def event_loop() -> typing.Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def async_db_engine(test_environment) -> typing.AsyncGenerator[AsyncEngine, None]:
    if await database_exists(settings().postgres_dsn):
        await drop_database(settings().postgres_dsn)

    await create_database(settings().postgres_dsn)

    engine = get_engine()
    await engine.dispose()

    yield engine

    await engine.dispose()
    await drop_database(settings().postgres_dsn)


@pytest.fixture(scope="session")
def apply_migrations() -> typing.Generator[None, None, None]:
    config = Config(os.path.join(settings().BASE_DIR, "alembic.ini"))
    config.set_main_option("script_location", os.path.join(settings().BASE_DIR, "migrations"))
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


@pytest_asyncio.fixture(scope="function")
async def async_db_session(async_db_engine: AsyncEngine, apply_migrations) -> typing.AsyncGenerator[AsyncSession, None]:
    async with async_db_engine.connect() as conn:
        async with conn.begin() as transaction:
            session = AsyncSession(bind=conn, expire_on_commit=False)

            yield session

            await transaction.rollback()
