from django.shortcuts import render
from rest_framework import generics

from .serializers.registration_serializer import RegistrationSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
