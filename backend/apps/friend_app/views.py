from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend

from apps.friend_app.models import FriendRequestModel, FriendListModel
from apps.friend_app.serializers import FriendRequestSerializer, SendFriendRequestSerializer, AlterFriendRequestSerializer, ListFriendsSerializer
from apps.components.permissions import IsRequestOwner


class ListFriendRequestsView(generics.ListAPIView):
    """
    API view for listing friend requests.

    This view provides a list of friend requests targeted to the currently authenticated user.
    It includes filtering capabilities, primarily focusing on the 'is_active' field of the friend requests.

    Attributes:
        - serializer_class (FriendRequestSerializer): The serializer class used for friend request instances.
        - permission_classes (list): Ensures that only authenticated users can access this view.
        - filter_backends (list): Specifies DjangoFilterBackend as the backend for filtering the queryset.
        - filterset_fields (list of str): Defines the fields on which the queryset can be filtered. In this case, 'is_active'.

    Methods:
        - get_queryset(self): Returns a queryset of FriendRequestModel instances where the receiver is the current user.
    """
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active']

    def get_queryset(self):
        return FriendRequestModel.objects.filter(receiver=self.request.user)


class SendFriendRequestView(generics.CreateAPIView):
    serializer_class = SendFriendRequestSerializer
    permission_classes = [IsAuthenticated]


class AcceptFriendRequestView(generics.UpdateAPIView):
    """
    API view for accepting a friend request.

    This view allows an authenticated user to accept a friend request. It uses the AlterFriendRequestSerializer and includes an additional permission to ensure that only the recipient of the friend request can accept it.

    Attributes:
        - permission_classes (list): Ensures that only authenticated users and the request owner can access this view.
        - serializer_class (AlterFriendRequestSerializer): Serializer for updating friend requests.

    Methods:
        - get_queryset(self): Returns friend requests where the current user is the receiver.
        - get_object(self): Retrieves a specific friend request based on the provided ID.
        - update(self, request, *args, **kwargs): Handles the acceptance of a friend request.
    """
    permission_classes = [IsAuthenticated, IsRequestOwner]
    serializer_class = AlterFriendRequestSerializer

    def get_queryset(self):
        return FriendRequestModel.objects.filter(receiver=self.request.user)

    def get_object(self):
        friend_request_id = self.kwargs.get('pk')
        try:
            return FriendRequestModel.objects.get(pk=friend_request_id, is_active=True)
        except FriendRequestModel.DoesNotExist:
            raise NotFound("Friend request not found.")

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.accept_friend_request()
        return Response({"detail": "Friend request accepted!"}, status=status.HTTP_200_OK)


class DeclineFriednRequestView(generics.DestroyAPIView):
    """
    API view for declining a friend request.

    This view allows an authenticated user to decline a friend request.
    It uses the AlterFriendRequestSerializer and includes an additional permission to ensure that only the recipient of the friend request can decline it.

    Attributes:
        - permission_classes (list): Ensures that only authenticated users and the request owner can access this view.
        - serializer_class (AlterFriendRequestSerializer): Serializer for updating friend requests.

    Methods:
        - get_queryset(self): Returns friend requests where the current user is the receiver.
        - get_object(self): Retrieves a specific friend request based on the provided ID.
        - destroy(self, request, *args, **kwargs): Handles the declining of a friend request.
    """
    permission_classes = [IsAuthenticated, IsRequestOwner]
    serializer_class = AlterFriendRequestSerializer

    def get_queryset(self):
        return FriendRequestModel.objects.filter(receiver=self.request.user)

    def get_object(self):
        friend_request_id = self.kwargs.get('pk')
        try:
            return FriendRequestModel.objects.get(pk=friend_request_id, is_active=True)
        except FriendRequestModel.DoesNotExist:
            raise NotFound("Friend request not found.")

    def destroy(self, request, *args, **kwargs):
        friend_request = self.get_object()
        friend_request.decline_friend_request()
        return Response({"details": "Friend request declined."}, status=status.HTTP_200_OK)


class ListFriendsView(generics.ListAPIView):
    """
    API view for listing friends.

    This view provides a list of friends for the currently authenticated user. It uses the ListFriendsSerializer to represent the friend data. Access to this view is restricted to authenticated users.

    Attributes:
        - permission_classes (list): Ensures that only authenticated users can access this view.
        - serializer_class (ListFriendsSerializer): Serializer for listing friends.

    Methods:
        - get_queryset(self): Returns the friend list of the current user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ListFriendsSerializer

    def get_queryset(self):
        return FriendListModel.objects.filter(owner=self.request.user)
