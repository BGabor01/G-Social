from rest_framework import serializers

from user_app.models import UserProfileModel


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating a user's profile picture.

    This serializer is specifically designed for the UserProfileModel, targeting
    the update of the profile picture.

    Fields:
        - profile_picture (ImageField): An ImageField required for updating the 
                                      profile picture of the user. It must be 
                                      provided when using this serializer.

    Meta:
        - model (Model): The UserProfileModel which this serializer is associated with.
        - fields (list): List containing 'profile_picture' to specify the only field
                       this serializer handles.
    """
    profile_picture = serializers.ImageField(required=True)

    class Meta:
        model = UserProfileModel
        fields = ['profile_picture']


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the complete user profile data.

    Meta:
        - model (Model): The UserProfileModel which this serializer is associated with.
        - fields (str): '__all__' indicates that all fields of UserProfileModel are to be
                      included in this serializer.
    """
    class Meta:
        model = UserProfileModel
        fields = '__all__'
