from django.urls import path

from apps.friend_app.views import ListFriendRequestsView, SendFriendRequestView, AcceptFriendRequestView, DeclineFriednRequestView, ListFriendsView

urlpatterns = [
    path('requests/list/', ListFriendRequestsView.as_view(),
         name='friend-request-list'),
    path('requests/send/', SendFriendRequestView.as_view(),
         name="friend-request-send"),
    path('requests/accept/<int:pk>/', AcceptFriendRequestView.as_view(),
         name="friend-request-accept"),
    path('requests/decline/<int:pk>/', DeclineFriednRequestView.as_view(),
         name="friend-request-decline"),
    path('list/', ListFriendsView.as_view(),
         name="friend-list")

]
