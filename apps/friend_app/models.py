from django.db import models
from django.contrib.auth.models import User


class FriendListModel(models.Model):
    """
    This model links users to their friends using a ManyToManyField, allowing for the creation and management of friend relationships.
    Each user can have their unique list of friends.

    Attributes:
        - owner (OneToOneField): A link to the User model. Represents the owner of the friend list.
        - friends (ManyToManyField): A set of User instances representing the friends of the owner.

    Methods:
        - __str__(self): Returns the username of the owner of the friend list.
        - is_friend(self, user: User): Checks if a given user is in the friend list.
        - add_friend(self, user: User): Adds a user to the friend list if not already present.
        - remove_friend(self, removee): Removes a user from the friend list if present.
        - unfriend(self, removee): Handles the mutual removal of friendship between two users.
    """
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='friend_list_owner')
    friends = models.ManyToManyField(
        User,  blank=True, related_name='friends')

    def __str__(self) -> str:
        """
        String representation of the FriendListModel instance.

        Returns:
            str: The username of the owner of the friend list.
        """
        return self.owner.username

    def is_friend(self, user: User) -> bool:
        """
        Check if a given user is in the friend list.

        Parameters:
            user (User): The user to check against the friend list.

        Returns:
            bool: True if the user is in the friend list, False otherwise.
        """
        return user in self.friends.all()

    def add_friend(self, user: User) -> None:
        """
        Add a user to the friend list.

        Adds the specified user to the friend list if they are not already a friend. 

        Parameters:
            user (User): The user to be added to the friend list.
        """
        if not self.is_friend(user):
            self.friends.add(user)

    def remove_friend(self, removee: User) -> None:
        """
        Remove a user from the friend list.

        Removes the specified user from the friend list if they are currently a friend.

        Parameters:
            removee (User): The user to be removed from the friend list.
        """
        if self.is_friend(removee):
            self.friends.remove(removee)

    def unfriend(self, removee: User) -> None:
        """
        Handles the mutual removal of friendship between two users.

        If both users are friends with each other, this method will remove each user from the other's friend list.

        Parameters:
            removee (User): The user with whom the friendship is to be terminated.
        """
        removee_friend_list_instance = FriendListModel.objects.get(
            owner=removee)
        if self.is_friend(removee) and removee_friend_list_instance.is_friend(self.owner):
            self.remove_friend(removee)
            removee_friend_list_instance.remove_friend(self.owner)


class FriendRequestModel(models.Model):
    """
    This model manages friend requests, including who sent the request, who received it, and whether the request is active or not.
    It also stores the date when the request was created.

    Attributes:
        - sender (ForeignKey): A reference to the User model for the user who sent the friend request.
        - receiver (ForeignKey): A reference to the User model for the user who received the friend request.
        - is_active (BooleanField): A flag indicating whether the friend request is active or not.
        - created_at (DateTimeField): The date and time when the friend request was created.

    Methods:
        - __str__(self): Returns the username of the sender of the friend request.
        - accept_friend_request(self): Handles the acceptance of a friend request.
        - decline_friend_request(self): Handles the decline of a friend request.
    """
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        """
        String representation of the FriendRequestModel instance.

        Returns:
            str: The username of the sender of the friend request.
        """
        return self.sender.username

    def accept_friend_request(self) -> None:
        """
        Handle the acceptance of a friend request.

        This method adds the sender to the receiver's friend list and vice versa.
        It also sets the friend request as inactive.
        """
        sender_friend_list = FriendListModel.objects.get(owner=self.sender)
        receiver_friend_list = FriendListModel.objects.get(owner=self.receiver)
        sender_friend_list.add_friend(self.receiver)
        receiver_friend_list.add_friend(self.sender)
        self.is_active = False
        self.save()

    def decline_friend_request(self) -> None:
        """
        Handle the decline of a friend request.

        This method sets the friend request as inactive without creating any new friend connections.
        """
        self.is_active = False
        self.save()
