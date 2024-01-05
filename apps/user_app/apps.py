from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_app'

    def ready(self):
        from apps.user_app.signals import user_created_signal
