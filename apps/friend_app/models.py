from django.db import models
from django.contrib.auth.models import User


class FriendListModel(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='friend_list_owner')
    friends = models.ManyToManyField(
        User,  blank=True, related_name='friends')

    def __str__(self):
        return self.owner.username

    def is_friend(self, user: User):
        return user in self.friends.all()

    def add_friend(self, user: User):
        if not self.is_friend(user):
            self.friends.add(user)

    def remove_friend(self, removee):
        if self.is_friend(removee):
            self.friends.remove(removee)

    def unfriend(self, removee):
        removee_friend_list_instance = FriendListModel.objects.get(
            owner=removee)
        if self.is_friend(removee) and removee_friend_list_instance.is_friend(self.owner):
            self.remove_friend(removee)
            removee_friend_list_instance.remove_friend(self.owner)


class FriendRequestModel(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.sender.username

    def accept_friend_request(self):
        sender_friend_list = FriendListModel.objects.get(owner=self.sender)
        receiver_friend_list = FriendListModel.objects.get(owner=self.receiver)
        sender_friend_list.add_friend(self.receiver)
        receiver_friend_list.add_friend(self.sender)
        self.is_active = False
        self.save()

    def decline_friend_request(self):
        self.is_active = False
        self.save()
