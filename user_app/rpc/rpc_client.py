import os
import time
from g_rpc import Client

welcome_rpc_client = Client("EMAIL_SENDER", host=os.environ.get("RABBITMQ_HOST"), username=os.environ.get("RABBITMQ_USER"), password=os.environ.get("RABBITMQ_PASS"))

