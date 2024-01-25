from django.urls import path
from apps.post_app.views import ListOrCreatePostView, UpdateOrDeletePostView, RetrievePostView

urlpatterns = [
    path('list/', ListOrCreatePostView.as_view(), name='create-post'),
    path('alter/<int:pk>/', UpdateOrDeletePostView.as_view(),
         name='update-or-delete-post'),
    path('retrieve/<int:pk>/', RetrievePostView.as_view(), name='retrieve-post'),
]
