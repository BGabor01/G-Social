from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from apps.friend_app.models import FriendRequestModel


@shared_task
def delete_expired_friend_requests():
    expiration_date = timezone.now() - timedelta(days=90)
    expired_requests = FriendRequestModel.objects.filter(
        created_at__lte=expiration_date)
    expired_requests.delete()
