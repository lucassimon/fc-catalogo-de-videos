## base image
FROM python:3.9-alpine AS compile-image

## install dependencies
RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add gcc && \
    apk add python3-dev && \
    apk add libffi-dev && \
    apk add postgresql-dev && \
    apk add gettext && \
    apk add gettext-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk add jpeg-dev && \
    apk add zlib-dev && \
    apk add libwebp-dev && \
    apk add libpng-dev && \
    apk add tiff-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers && \
    rm -rf /var/cache/apk/*

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r prod.txt


## build-image
FROM python:3.9-alpine AS runtime-image

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/home/api PATH="/opt/venv/bin:$PATH" LIBRARY_PATH=/lib:/usr/lib

## copy Python dependencies from build image
COPY --from=compile-image /opt/venv /opt/venv


## install dependencies
RUN apk update && \
    apk add --no-cache libpq && \
    apk add --no-cache gettext && \
    apk add --no-cache jpeg-dev && \
    apk add --no-cache zlib-dev && \
    apk add --no-cache libwebp-dev && \
    apk add --no-cache libpng-dev && \
    apk add --no-cache tiff-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers


## add user
RUN adduser -D api
USER api:api
WORKDIR $HOME
COPY --chown=api:api . $HOME
COPY --chown=api:api ./entrypoint.sh /entrypoint.sh
COPY --chown=api:api ./start.sh /start.sh

EXPOSE 5000
ENTRYPOINT [ "/entrypoint.sh" ]

