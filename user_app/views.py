from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from user_app.serializers import RegistrationSerializer, UserDataSerializer, UserProfileUpdateSerializer
from user_app.permissions.IsOwnerPermission import IsOwner
from user_app.models import UserProfileModel


class CreateUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer


class RetrieveUserDataView(generics.RetrieveAPIView):
    serializer_class = UserDataSerializer
    queryset = User.objects.all()


class UpdateProfileView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = UserProfileUpdateSerializer
    queryset = UserProfileModel.objects.all()
