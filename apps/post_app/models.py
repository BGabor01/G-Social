from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    """
    Model representing a post in a social media application.

    This model defines a post with attributes for the owner (a user), text content, an image, and the creation time of the post.
    The owner is linked via a ForeignKey to the User model, establishing a many-to-one relationship.
    The text field is a character field that can be blank, allowing for image-only posts.
    The image is stored in a specified directory and can also be left blank for text-only posts.
    The creation time is automatically set when a new instance is created and indexed for efficient querying.

    Attributes:
        - owner (ForeignKey): A reference to the User model, representing the user who owns the post.
        - text (CharField): The text content of the post, can be blank.
        - image (ImageField): An image associated with the post, can be blank. Stored in 'user_pics'.
        - created_at (DateTimeField): The timestamp when the post was created, automatically set.

    Methods:
        - __str__(self): Returns a string representation of the post, typically used for debugging purposes.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_owner")
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="user_pics")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.owner.username}'s post"
