from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.post_app.serializers import PostSerializer
from apps.post_app.models import PostModel
from apps.post_app.paginations import PostCursorPagination
from apps.components.permissions import IsOwner


class ListOrCreatePostView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = PostCursorPagination
    queryset = PostModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UpdateOrDeletePostView(generics.UpdateAPIView, generics.DestroyAPIView):

    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

class RetrievePostView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()