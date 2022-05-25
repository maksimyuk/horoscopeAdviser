# pull official base image
FROM python:3.10.4-slim-buster

# set environment variables
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  # poetry:
  PATH=/root/.local/bin:$PATH

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    bash \
    curl \
    wget \
    # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# install poetry dependences
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false

# set work directory
WORKDIR /code

RUN poetry install

# copy project
COPY . /code
