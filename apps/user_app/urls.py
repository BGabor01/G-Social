from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user_app.views import CreateUserView, UpdateProfileView, RetrieveUserDataView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('update-profile/<int:pk>/',
         UpdateProfileView.as_view(), name='update-profile'),
    path('retrieve-user/<int:pk>/',
         RetrieveUserDataView.as_view(), name="retrieve_user")
]
