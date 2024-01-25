from rest_framework import serializers
from apps.friend_app.models import FriendRequestModel


class AlterFriendRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for altering friend requests.

    This serializer is tailored for updating specific fields of existing FriendRequestModel instances.
    It allows for modification of the 'is_active' field, while keeping the 'receiver' field read-only.
    This is particularly useful for updating the status of friend requests without altering the receiver.

    Meta:
        - model (FriendRequestModel): The model associated with this serializer.
        - fields (list of str): Fields of the FriendRequestModel that are included in the serialized output. Includes 'id', 'receiver', and 'is_active'.
        - read_only_fields (list of str): Fields that are marked as read-only. In this case, 'receiver'.
    """
    class Meta:
        model = FriendRequestModel
        fields = ['id', 'receiver', 'is_active']
        read_only_fields = ['receiver']
