ARG BASE_IMAGE=python:3.8-slim-buster
FROM ${BASE_IMAGE}

# system update & package install
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openssl libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 一般ユーザーアカウントを追加
ENV USER_NAME=app
ARG USER_UID=1000
ARG PASSWD=password

RUN useradd -m -s /bin/bash -u ${USER_UID} ${USER_NAME} && \
    gpasswd -a ${USER_NAME} sudo && \
    echo "${USER_NAME}:${PASSWD}" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) ALL" >> /etc/sudoers
# 一般ユーザーにsudo権限を付与
#RUN gpasswd -a ${UID} sudo


# https://medium.com/@rlagowski/create-flask-app-with-uwsgi-nginx-certbot-for-ssl-and-all-this-with-docker-a9f23516618d
# 運用時はコンテナイメージ内にソースコードを含める
COPY ./app /app/app
COPY ./pyproject.toml /app/pyproject.toml
# COPY ./poetry.lock /app/poetry.lock
RUN chown -R ${USER_NAME}:${USER_NAME} /app


USER ${USER_UID}
# WORKDIR /tmp/app_env
WORKDIR /app
# pip & poetry
ENV PATH $PATH:/home/${USER_NAME}/.local/bin
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install poetry --user && \
    poetry config virtualenvs.in-project true && \
    poetry install && \
    rm -rf ~/.cache/pip/* && \
    rm -rf ~/.cache/pypoetry/*

# Configration
EXPOSE 8000

# Execute
ENV PATH=/app/.venv/bin:$PATH
# ENTRYPOINT ["poetry", "shell"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--proxy-headers", "--forwarded-allow-ips", "*"]
