from rest_framework import serializers
from django.contrib.auth.models import User

from user_app.serializers import ProfileSerializer


class UserDataSerializer(serializers.ModelSerializer):
    """
    A serializer for user data along with their profile information.

    This serializer is used for serializing the data of a User model instance, including
    associated profile data. In addition to the basic user fields like username, first name,
    last name, and email, this serializer includes a nested ProfileSerializer.

    Fields:
        - profile_data (ProfileSerializer): A nested serializer for the user's profile data.
                                          It is read-only and used to present the associated
                                          profile information alongside the basic user data.

    Meta:
        - model (Model): The User model from Django's authentication system.
        - fields (list): Specifies the fields to be included in the serialization - username,
                       first name, last name, email, and profile_data for the user's profile.
    """
    profile_data = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'profile_data']
