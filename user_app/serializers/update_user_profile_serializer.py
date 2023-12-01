from rest_framework import serializers

from user_app.models import UserProfileModel


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=True)

    class Meta:
        model = UserProfileModel
        fields = ["profile_picture"]
