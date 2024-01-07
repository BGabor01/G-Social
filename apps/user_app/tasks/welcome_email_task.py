import os
import logging

from celery import shared_task

from g_rpc import Client

logger = logging.getLogger('user_app')

@shared_task
def send_welcome_email(email: str | bytes):
    """
    Asynchronous task for sending a welcome email.

    This function sends a welcome email to a new user using a remote procedure call to an email sender service.
    It handles connection details to the RabbitMQ server and logs the outcome.

    Parameters:
        - email (str | bytes): The email address to which the welcome email is sent.
    """
    try:
        welcome_rpc_client = Client('EMAIL_SENDER', host=os.environ.get('RABBITMQ_HOST', 'localhost'), username=os.environ.get('RABBITMQ_USER','guest'), password=os.environ.get('RABBITMQ_PASS','guest'))
        welcome_rpc_client.send_request('registration', email)
        logger.info('Welcome e-mail sent!')
    except TimeoutError as e:
        logger.error(e)