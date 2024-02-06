from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.post_app.serializers import PostSerializer
from apps.post_app.models import PostModel
from apps.post_app.paginations import PostCursorPagination
from apps.components.permissions import IsOwner


class ListOrCreatePostView(generics.ListCreateAPIView):
    """
    API view for listing or creating posts.

    This view allows authenticated users to either list existing posts or create new ones.
    It utilizes the PostSerializer for serializing and validating posts.

    Attributes:
        - permission_classes (list): Ensures that the user is authenticated.
        - serializer_class (ModelSerializer): The serializer class used for posts.
        - pagination_class (CursorPagination): The pagination class used to paginate the results.
        - queryset (QuerySet): The queryset containing all PostModel instances.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    pagination_class = PostCursorPagination
    queryset = PostModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UpdateOrDeletePostView(generics.UpdateAPIView, generics.DestroyAPIView):
    """
    API view for updating or deleting a post.

    This view allows authenticated users, who are also the owners of the post, to update or delete their posts.
    It checks if the user is authenticated and is the owner of the post.

    Attributes:
        - permission_classes (list): Ensures that the user is authenticated and is the owner of the post.
        - serializer_class (ModelSerializer): The serializer class used for posts.
        - queryset (QuerySet): The queryset containing all PostModel instances.
    """
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()


class RetrievePostView(generics.RetrieveAPIView):
    """
    API view for retrieving a single post.

    This view allows authenticated users to retrieve the details of a specific post.
    It ensures that the user is authenticated before providing access to the post data.

    Attributes:
        - permission_classes (list): Ensures that the user is authenticated.
        - serializer_class (ModelSerializer): The serializer class used for posts.
        - queryset (QuerySet): The queryset containing all PostModel instances.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
