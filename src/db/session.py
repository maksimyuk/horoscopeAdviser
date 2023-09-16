import functools
import typing

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings


@functools.lru_cache
def get_engine(url: str | URL | None = settings().postgres_dsn, **kwargs) -> AsyncEngine:
    return create_async_engine(url, echo=False, future=True, **kwargs)


def get_async_session(
    url: str | URL | None = settings().postgres_dsn,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(get_engine(url), expire_on_commit=False)


async def get_session() -> typing.AsyncGenerator[AsyncSession, None]:
    async_session = get_async_session()
    async with async_session() as session:
        yield session
