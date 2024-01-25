from rest_framework import serializers
from apps.friend_app.models import FriendRequestModel


class SendFriendRequestSerializer(serializers.ModelSerializer):
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
