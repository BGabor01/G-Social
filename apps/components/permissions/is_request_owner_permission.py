from django.http import HttpRequest
from rest_framework import permissions
from rest_framework import generics
from django.db import models


class IsRequestOwner(permissions.BasePermission):

    def has_object_permission(self, request: HttpRequest, view: generics.GenericAPIView, obj: models.Model) -> bool:

        return obj.receiver == request.user
