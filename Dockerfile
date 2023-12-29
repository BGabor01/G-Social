FROM python:3.11-alpine

WORKDIR /usr/src/app/

# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure python output is sent directly to the terminal
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache git mariadb-dev build-base

RUN pip install pipenv --no-cache

COPY ./Pipfile ./Pipfile

RUN pipenv install

COPY . .
