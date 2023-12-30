FROM python:3.11-alpine
# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure python output is sent directly to the terminal
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache git mariadb-dev build-base netcat-openbsd

RUN pip install pipenv --no-cache

WORKDIR /usr/src/app/

COPY ./Pipfile ./Pipfile
COPY ./bash_scripts/celey_entrypoint.sh ./celey_entrypoint.sh
COPY ./bash_scripts/django_entrypoint.sh ./django_entrypoint.sh
COPY ./bash_scripts/wait_for_service.sh ./wait_for_service.sh

RUN chmod +x ./django_entrypoint.sh
RUN chmod +x ./celey_entrypoint.sh
RUN chmod +x ./wait_for_service.sh
RUN pipenv install

COPY . .