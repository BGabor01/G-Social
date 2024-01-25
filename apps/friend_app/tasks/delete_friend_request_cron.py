from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from apps.friend_app.models import FriendRequestModel


@shared_task
def delete_expired_friend_requests():
    """
    A Celery task that deletes expired friend requests.

    This scheduled task runs periodically to clean up the FriendRequestModel by deleting friend requests that are older than 90 days.
    This helps in maintaining the database and removing outdated data.
    """
    expiration_date = timezone.now() - timedelta(days=90)
    expired_requests = FriendRequestModel.objects.filter(
        created_at__lte=expiration_date)
    expired_requests.delete()
