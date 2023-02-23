# https://github.com/marciovrl/fastapi/blob/master/Dockerfile
# pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /fastapi_implement/sql_app

# copy requirements file
COPY requirements.txt .
# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    postgresql-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /src/requirements.txt \
    && rm -rf /root/.cache/pip
COPY . .
CMD uvicorn sql_app.main:app --reload --workers 1 --host 0.0.0.0 --port 8080


# FROM python:3.8-slim
# WORKDIR /fastapi_implement
#
# COPY requirements.txt .
# RUN pip install --upgrade pip && \
#     pip install wheel  && \
#     pip install -r requirements.txt --no-cache-dir
#
# COPY . .
#
# CMD uvicorn demo:app --reload --workers 1 --host 0.0.0.0 --port 8080
# # CMD [ "python", "./demo.py" ]
