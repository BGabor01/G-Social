#!/bin/sh

. ./wait_for_service.sh

# Wait for RabbitMQ to be ready
wait_for_service $RABBITMQ_HOST 5672  

pipenv run celery -A g_social worker --loglevel=info