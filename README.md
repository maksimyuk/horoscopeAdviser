# Horoscope adviser Backend
Small app, that can give you horoscope from different sources.

![alt text](https://img.shields.io/badge/python-3.10.12-orange)


## Technology stack

1. FastAPI
2. SQLAlchemy + Alembic
3. PostgreSQL
4. aiohttp
5. Docker, docker compose

## Development

#### Make lint, tests
```shell
make -C src lint
make -C src test
```

## Migrations

#### Generate new migration
```shell
cd src/
alembic revision --autogenerate -m "Migration Name"
```

#### Run migrations
```shell
cd src/
alembic upgrade head
```

#### Downgrade last migration
```shell
cd src/
alembic downgrade -1
```