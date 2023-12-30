from g_social.settings.settings import *

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

ALLOWED_HOSTS = ['django','127.0.0.1','localhost']

USE_X_FORWARDED_HOST = True

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

DEBUG = False
