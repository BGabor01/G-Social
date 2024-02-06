import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          f'g_social.settings.settings_{os.environ.get("ENVIRONMENT")}')

app = Celery('your_project')

# Using Redis as broker
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()