import functools
import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

from .const import TEST_ENVIRONMENT_NAME

_BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
_CONFIG_DIR: pathlib.Path = _BASE_DIR.parent.joinpath("config")


class Settings(BaseSettings):
    """Project settings."""

    BASE_DIR: pathlib.Path = _BASE_DIR

    model_config = SettingsConfigDict(
        env_file=_CONFIG_DIR.joinpath(".env"), env_file_encoding="utf-8"
    )

    ENVIRONMENT: str = "local"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "horoscope_adviser"

    TELEGRAM_SECRET_TOKEN: str | None = None

    SHOW_HOROSCOPE_SOURCE: bool = True

    @property
    def postgres_dsn(self) -> str:
        database = (
            self.POSTGRES_DB
            if self.ENVIRONMENT != TEST_ENVIRONMENT_NAME
            else f"{self.POSTGRES_DB}_test"
        )
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database}"
        )


@functools.lru_cache
def settings() -> Settings:
    return Settings()
