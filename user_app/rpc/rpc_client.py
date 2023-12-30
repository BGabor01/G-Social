import os
import time
from g_rpc import Client

welcome_rpc_client = Client("EMAIL_SENDER", host=os.environ.get("RABBITMQ_HOST", "localhost"), username=os.environ.get("RABBITMQ_USER","guest"), password=os.environ.get("RABBITMQ_PASS","guest"))

