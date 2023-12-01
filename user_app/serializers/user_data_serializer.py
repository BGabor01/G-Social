from rest_framework import serializers
from django.contrib.auth.models import User

from user_app.serializers import ProfileSerializer


class UserDataSerializer(serializers.ModelSerializer):
    profile_data = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'profile_data']
