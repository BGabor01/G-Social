from rest_framework import generics
from rest_framework import permissions

from .serializers.registration_serializer import RegistrationSerializer
from .serializers.update_user_profile_serializer import UserProfileUpdateSerializer
from user_app.permissions.IsOwnerPermission import IsOwner


class CreateUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class UpdateProfileView(generics.UpdateAPIView):
    authentication_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserProfileUpdateSerializer
