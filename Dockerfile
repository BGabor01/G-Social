FROM python:3.11-alpine
# Prevent python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure python output is sent directly to the terminal
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache git mariadb-dev build-base netcat-openbsd

RUN pip install pipenv --no-cache

WORKDIR /usr/src/app/

COPY ./Pipfile ./Pipfile
COPY ./entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh
RUN pipenv install

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]