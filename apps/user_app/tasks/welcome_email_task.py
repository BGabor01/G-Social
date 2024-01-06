import os
import logging

from celery import shared_task

from g_rpc import Client

logger = logging.getLogger('user_app')

@shared_task
def send_welcome_email(email: str | bytes):
    try:
        welcome_rpc_client = Client('EMAIL_SENDER', host=os.environ.get('RABBITMQ_HOST', 'localhost'), username=os.environ.get('RABBITMQ_USER','guest'), password=os.environ.get('RABBITMQ_PASS','guest'))
        welcome_rpc_client.send_request('registration', email)
        logger.info('Welcome e-mail sent!')
    except TimeoutError as e:
        logger.error(e)