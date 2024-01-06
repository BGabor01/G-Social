from django.urls import path
from apps.post_app.views import CreatePostView, UpdateOrDeletePostView, RetrievePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('alter/<int:pk>/', UpdateOrDeletePostView.as_view(), name='update-or-delete-post'),
    path('retrieve/<int:pk>/', RetrievePostView.as_view(), name='retrieve-post'),
]
