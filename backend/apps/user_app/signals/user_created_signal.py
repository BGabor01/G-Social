import os

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from apps.user_app.models import UserProfileModel
from apps.friend_app.models import FriendListModel
from apps.user_app.tasks.welcome_email_task import send_welcome_email

import logging
logger = logging.getLogger("user_app")


@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **kwargs) -> None:
    """
    Signal receiver that creates a user profile and sends a welcome notification
    when a new User instance is created.

    This function is connected to Django's post_save signal for the User model. 
    Whenever a new User instance is saved for the first time (i.e., created), 
    it automatically creates an associated UserProfileModel instance for that user
    and sends a welcome notification using a remote procedure call (RPC).

    Parameters:
        - sender (User): The model class that sent the signal. In this case, User.
        - instance (User): The instance of the User model that was saved.
        - created (bool): A boolean flag indicating whether this is a new instance 
                        (True) or an update to an existing instance (False).
        - **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfileModel.objects.create(owner=instance)
        logger.info('Profile created!')

        FriendListModel.objects.create(owner=instance)
        logger.info("Friend list created!")
        if not settings.DEBUG:
            send_welcome_email.delay(instance.email)
