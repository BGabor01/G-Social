from rest_framework import serializers

from apps.friend_app.models import FriendRequestModel


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FriendRequestModel
