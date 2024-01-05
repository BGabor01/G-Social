from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from apps.user_app.serializers import RegistrationSerializer, UserDataSerializer, UserProfileUpdateSerializer
from apps.user_app.permissions.IsOwnerPermission import IsOwner
from apps.user_app.models import UserProfileModel


class CreateUserView(generics.CreateAPIView):
    """
    API view for creating new users.

    This view handles the creation of new users in the system.

    Attributes:
        - serializer_class (ModelSerializer): The serializer class used for validating and
                                       serializing input data for creating a new user.
    """
    serializer_class = RegistrationSerializer


class RetrieveUserDataView(generics.RetrieveAPIView):
    """
    API view for retrieving a user's data.

    This view is used to retrieve the details of a specific user. It is set up to
    work with all User model instances.

    Attributes:
        - serializer_class (ModelSerializer): The serializer class used for serializing the
                                       user data.
        - queryset (QuerySet): The queryset that contains all the User model instances,
                             from which the specific user data is retrieved.
    """
    serializer_class = UserDataSerializer
    queryset = User.objects.all()


class UpdateProfileView(generics.UpdateAPIView):
    """
    API view for updating a user's profile.

    This view allows authenticated users to update their profile. It checks if the
    user is authenticated and is the owner of the profile before allowing an update.

    Attributes:
        - permission_classes (list): A list of permission classes applied to this view.
                                   It ensures that the user is authenticated and is the
                                   owner of the profile.
        - serializer_class (ModelSerializer): The serializer class used for validating and
                                       serializing the input data for profile updates.
        - queryset (QuerySet): The queryset containing all UserProfileModel instances,
                             from which the specific user profile is retrieved for updating.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserProfileUpdateSerializer
    queryset = UserProfileModel.objects.all()
