from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_app.models import UserProfileModel


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)
