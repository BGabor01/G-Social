"""
WSGI config for g_social project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          f'g_social.settings.settings_{os.environ.get("ENVIRONMENT")}')

application = get_wsgi_application()
