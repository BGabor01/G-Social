#!/bin/sh

# Function to check if a service is ready by trying to connect to a given host and port
wait_for_service() {
    local host=$1
    local port=$2
    echo "Waiting for $host to be ready..."
    while ! nc -z $host $port; do
        sleep 0.1
    done
    echo "$host is ready!"
}

# Wait for the database to be ready
wait_for_service $DATABASE_HOST $DATABASE_PORT

# Wait for RabbitMQ to be ready
wait_for_service $RABBITMQ_HOST 5672  # 5672 is the default port for RabbitMQ

# Apply database migrations
echo "Applying database migrations..."
pipenv run python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
pipenv run python manage.py collectstatic --noinput --clear

# Start Gunicorn server
exec "$@"
