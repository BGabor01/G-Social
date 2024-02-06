from django.contrib import admin
from apps.friend_app.models import FriendListModel, FriendRequestModel

# Register your models here.

admin.site.register(FriendListModel)
admin.site.register(FriendRequestModel)
