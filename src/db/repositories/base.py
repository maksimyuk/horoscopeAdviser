from sqlalchemy.ext.asyncio import AsyncSession


class BaseDatabaseRepository:
    _session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
