from g_social.settings.settings import *

from celery.schedules import crontab

DEBUG = False

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

ALLOWED_HOSTS = ['django', '127.0.0.1', 'localhost']

USE_X_FORWARDED_HOST = True

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

CELERY_BEAT_SCHEDULE = {
    'delete_expired_friend_requests_everyday': {
        'task': 'apps.friend_app.tasks.delete_friend_request_cron.delete_expired_friend_requests',
        'schedule': crontab(hour=0, minute=0),
    },
}
