from rest_framework.pagination import CursorPagination


class PostCursorPagination(CursorPagination):
    """
    Cursor pagination for post instances.

    This class defines the pagination behavior for listing posts,
    with a specified page size and ordering based on the creation date of the posts.

    Attributes:
        - page_size (int): The number of items per page.
        - ordering (str): The ordering of the posts in the result set, by default ordered by 'created_at' in descending order.
    """
    page_size = 30
    ordering = '-created_at'
