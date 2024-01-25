from rest_framework import serializers

from apps.friend_app.models import FriendRequestModel


class FriendRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for friend requests.

    This serializer is designed for handling FriendRequestModel instances.
    It serializes all fields of the FriendRequestModel, providing a comprehensive representation of friend requests.

    Meta:
        - model (FriendRequestModel): The model associated with this serializer, representing friend requests.
        - fields (str): Indicates that all fields of the FriendRequestModel are included in the serialized output.
    """
    class Meta:
        fields = '__all__'
        model = FriendRequestModel
