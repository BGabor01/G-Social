#!/bin/sh

. ./bash_scripts/wait_for_service.sh

# Wait for the database to be ready
wait_for_service $DATABASE_HOST $DATABASE_PORT

# Wait for RabbitMQ to be ready
wait_for_service $RABBITMQ_HOST 5672  

# Apply database migrations
echo "Applying database migrations..."
pipenv run python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
pipenv run python manage.py collectstatic --noinput --clear

#Start Gunicorn server
pipenv run gunicorn -c g_social/gunicorn.conf.py g_social.wsgi:application --bind 0.0.0.0:8000
