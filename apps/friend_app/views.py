from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend

from apps.friend_app.models import FriendRequestModel, FriendListModel
from apps.friend_app.serializers import FriendRequestSerializer, SendFriendRequestSerializer, AlterFriendRequestSerializer, ListFriendsSerializer


class ListFriendRequestsView(generics.ListAPIView):
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
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
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
