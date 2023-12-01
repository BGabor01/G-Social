from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user_app.views import CreateUserView, UpdateProfileView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('update-profile/<int:pk>/',
         UpdateProfileView.as_view(), name='update-profile')
]
