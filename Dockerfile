FROM python:3.6.15

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.11
RUN pip3 install cryptography==2.3 \
    && pip3 install Cython \
    && pip3 install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . /app/

EXPOSE 3000

CMD ["/bin/bash", "/app/dagster-dagit-start.sh"]
