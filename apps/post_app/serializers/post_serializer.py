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

    def validate(self, data):
        if not data.get('text') and not data.get('image'):
            raise serializers.ValidationError(
                "At least one of 'text' or 'image' must be provided.")

        return data
