# Use a specific version of the python alpine image for consistency
FROM python:3.11.7-alpine

# Set environment variables to prevent Python from writing .pyc files
# and to ensure Python output is sent directly to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update && apk add --no-cache git mariadb-dev build-base netcat-openbsd && \
    rm -rf /var/cache/apk/*

RUN pip install pipenv --no-cache-dir

WORKDIR /usr/src/app/

COPY ./Pipfile ./Pipfile

# Install Python dependencies using pipenv
RUN pipenv install

COPY . .

# Set permissions for entrypoint scripts
RUN chmod +x ./bash_scripts/*.sh