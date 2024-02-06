from django.http import HttpRequest
from rest_framework import permissions
from rest_framework import generics
from django.db import models


class IsRequestOwner(permissions.BasePermission):
    """
    Custom permission to only allow receiver of a friend request to edit it.

    This class extends the BasePermission class from Django REST framework's
    permissions module. It overrides the has_object_permission.

    Methods:
        - has_object_permission: Checks if the request user is the reciever of the request.

    Usage:
        - This permission can be applied to views by including it in the view's
        'permission_classes' list.
    """

    def has_object_permission(self, request: HttpRequest, view: generics.GenericAPIView, obj: models.Model) -> bool:

        return obj.receiver == request.user
