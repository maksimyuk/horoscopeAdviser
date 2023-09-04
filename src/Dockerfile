FROM python:3.10.13-slim

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
  && apt install -y netcat-traditional make \
  && pip install --upgrade pip \
  && pip install poetry==1.4.2

# install poetry dependences
COPY ./src/pyproject.toml ./src/poetry.lock ./

ARG DEV_DEPS=False

RUN poetry config virtualenvs.create false
RUN if [ $DEV_DEPS = True ] ; then \
  poetry install --no-interaction --no-ansi ; else \
  poetry install --only main --no-interaction --no-ansi ; fi

# copy project
COPY . .

RUN chmod 777 /usr/src/app/src/entrypoint.sh
ENTRYPOINT ["/usr/src/app/src/entrypoint.sh"]
