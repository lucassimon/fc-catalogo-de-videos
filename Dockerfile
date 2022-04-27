## base image
FROM python:3.10-alpine AS compile-image

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
RUN pip install -r dev.txt


## build-image
FROM python:3.10-alpine AS runtime-image

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOME=/home/api \
    PATH="/opt/venv/bin:$PATH" \
    LIBRARY_PATH=/lib:/usr/lib \
    JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64


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
    apk add --no-cache git && \
    apk add --no-cache git-flow && \
    apk add --no-cache curl && \
    apk add --no-cache wget && \
    apk add --no-cache vim && \
    apk add --no-cache zsh && \
    apk add --no-cache openjdk8-jre && \
    apk add --no-cache --virtual .build-deps build-base linux-headers && \
    rm -rf /var/cache/apk/*

## add user
RUN adduser -D api
USER api:api
WORKDIR $HOME

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t "ys" \
    -p git \
    -p git-flow \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zdharma/fast-syntax-highlighting \
    -a "export TERM=xterm-256color"
# && echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc


COPY --chown=api:api ./.devcontainer/entrypoint.sh $HOME/entrypoint.sh
COPY --chown=api:api ./.devcontainer/start.sh $HOME/start.sh
COPY --chown=api:api ./.devcontainer/gitconfig $HOME/.gitconfig

EXPOSE 5000
ENTRYPOINT [ "/home/api/entrypoint.sh" ]

