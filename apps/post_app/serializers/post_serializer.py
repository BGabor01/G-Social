from rest_framework import serializers

from apps.post_app.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for PostModel instances.

    This serializer handles the serialization and validation of PostModel instances.
    It includes fields for the owner, text, and image of a post. The 'owner' field is read-only.

    Meta:
        - model (Model): The PostModel class that this serializer works with.
        - fields (list of str): The fields included in the serialization ('owner', 'text', 'image').
        - read_only_fields (list of str): Fields that are read-only ('owner').

    Methods:
        - validate(data): Validates the input data, ensuring that either 'text' or 'image' is provided.
    """
    class Meta:
        model = PostModel
        fields = ['owner', 'text', 'image']
        read_only_fields = ['owner']

    def validate(self, data: dict) -> dict:
        """
        Validates the friend request data.

        Checks if the sender and receiver are the same, indicating a user trying to send a friend request to themselves. Also checks for an existing active friend request between the same sender and receiver to prevent duplicate requests.

        Parameters:
            - data (dict): The data to be validated, containing sender and receiver information.

        Returns:
            dict: The validated data.

        Raises:
            ValidationError: If the sender and receiver are the same or if a duplicate friend request exists.
        """
        if not data.get('text') and not data.get('image'):
            raise serializers.ValidationError(
                "At least one of 'text' or 'image' must be provided.")

        return data
