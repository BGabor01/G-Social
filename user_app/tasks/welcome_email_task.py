import logging

from celery import shared_task

from user_app.rpc import welcome_rpc_client

logger = logging.getLogger("user_app")

@shared_task
def send_welcome_email(email: str | bytes):
    try:
        welcome_rpc_client.send_request("registration", email)
        logger.info("Welcome e-mail sent!")
    except TimeoutError as e:
        logger.error(e)