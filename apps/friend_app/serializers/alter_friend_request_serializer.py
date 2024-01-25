from rest_framework import serializers
from apps.friend_app.models import FriendRequestModel


class AlterFriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequestModel
        fields = ['id', 'receiver', 'is_active']
        read_only_fields = ['receiver']
