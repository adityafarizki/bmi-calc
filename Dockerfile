FROM python:3.8-slim

COPY scripts /scripts
COPY pyproject.toml /
COPY poetry.lock /
RUN python -m pip install --no-cache-dir poetry \
    && python -m poetry export --without-hashes -f requirements.txt > requirements.txt \
    && python -m pip install -r requirements.txt

RUN apt update && apt install -y dumb-init

COPY ./ /app
WORKDIR /app

ENTRYPOINT ["dumb-init", "--"]
CMD [ "/bin/sh", "scripts/start_prod.sh" ]
