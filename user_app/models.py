from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile_data")
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"
