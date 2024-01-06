from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="user_pics")

    def __str__(self) -> str:
        return f"{self.owner.username}'s post"