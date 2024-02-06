from django.http import HttpRequest
from rest_framework import permissions
from rest_framework import generics
from django.db import models


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    This class extends the BasePermission class from Django REST framework's
    permissions module. It overrides the has_object_permission method to check
    whether the user making the request is the 'owner' of the object.

    Methods:
        - has_object_permission: Checks if the request user is the owner of the object.

    Usage:
        - This permission can be applied to views by including it in the view's
        'permission_classes' list.
    """

    def has_object_permission(self, request: HttpRequest, view: generics.GenericAPIView, obj: models.Model) -> bool:
        """
        Check if the user making the request is the owner of the object.

        Parameters:
            - request (HttpRequest): The HTTP request from the user.
            - view (GenericAPIView): The view which this permission is applied to.
            - obj (Model instance): The object that is being accessed or manipulated.

        Returns:
            bool: True if the request user is the owner of the object, False otherwise.
        """
        return obj.owner == request.user
