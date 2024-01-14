from rest_framework import serializers

from apps.friend_app.models import FriendListModel


class ListFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FriendListModel
