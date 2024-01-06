from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    """
    UserProfileModel represents a user's profile information in the system.

    This model is designed to extend the basic User model provided by Django's
    authentication system. It includes additional fields that are specific to the
    user's profile, such as their profile picture.

    Attributes:
        - owner (User): A OneToOneField to the User model. This field links the
                      UserProfileModel to User model, establishing
                      a one-to-one relationship between a user and their profile.
                      On deletion of the User, the related UserProfileModel instance
                      will also be deleted (models.CASCADE).
        - profile_picture (ImageField): An ImageField to store the user's profile picture.
                                      If no image is provided, a default image is used.
                                      Images are uploaded to the 'profile_pics' directory.

    Methods:
        - __str__: Returns a human-readable representation of the UserProfileModel instance,
                 which is the username of the owner appended with 's profile'.
    """
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile_data')
    profile_picture = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"
