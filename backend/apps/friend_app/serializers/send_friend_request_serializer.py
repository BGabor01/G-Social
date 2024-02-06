from rest_framework import serializers
from apps.friend_app.models import FriendRequestModel


class SendFriendRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for sending a friend request.

    This serializer is used for creating friend requests. It ensures that the sender of the request is automatically set to the current user and that the receiver is specified. It includes validation to prevent users from sending friend requests to themselves and to avoid duplicate friend requests.

    Attributes:
        - sender (HiddenField): Automatically set to the current user, not visible to the user.

    Meta:
        - model (FriendRequestModel): The model associated with this serializer.
        - fields (list of str): Specifies which fields should be included in the serialized output. 
    """
    sender = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = FriendRequestModel
        fields = ['sender', 'receiver']

    def validate(self, data):
        if data['sender'] == data['receiver']:
            raise serializers.ValidationError(
                {"receiver": "Can't send friend request to yourself!"})

        if FriendRequestModel.objects.filter(sender=data['sender'], receiver=data['receiver'], is_active=True).exists():
            raise serializers.ValidationError(
                {"receiver": "A friend request already exists."})

        return data
