# Friend App Details

## Models

| Model                | Description                                                               |
|----------------------|---------------------------------------------------------------------------|
| `FriendListModel`    | Manages user's friends list, linking users to their friends.              |
| `FriendRequestModel` | Handles friend requests   |

## Views

| View                        | Description                                                                                                  | Serializer                        |
|-----------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `SendFriendRequestView`     | API view for sending a friend request. Allows authenticated users to send friend requests.                   | `SendFriendRequestSerializer`     |
| `AcceptFriendRequestView`   | API view for accepting a friend request. Authenticated users can accept friend requests sent to them.        | `AlterFriendRequestSerializer`    |
| `DeclineFriendRequestView`  | API view for declining a friend request. Authenticated users can decline friend requests sent to them.      | `AlterFriendRequestSerializer`    |
| `ListFriendRequestsView`    | API view for listing friend requests. Lists friend requests targeted to the authenticated user.              | `FriendRequestSerializer`         |
| `ListFriendsView`           | API view for listing friends. Lists all friends of the authenticated user.                                  | `ListFriendsSerializer`           |

## Permissions

| Permission              | Description                                                       |
|-------------------------|-------------------------------------------------------------------|
| `IsAuthenticated`       | Ensures that the user is authenticated.                           |
| `IsRequestOwner`        | Ensures that the user is the owner of the friend request.         |

## Serializers

| Serializer                      | Description                                                                     |
|---------------------------------|---------------------------------------------------------------------------------|
| `FriendRequestSerializer`       | Serializes all fields of the FriendRequestModel.                                |
| `SendFriendRequestSerializer`   | Serializes the sending of friend requests, with automatic sender recognition.   |
| `AlterFriendRequestSerializer`  | Serializes the updating of friend requests, mainly for accepting/declining.     |
| `ListFriendsSerializer`         | Serializes the listing of friends, showing all details from FriendListModel.    |

## Filters

| Filter                  | Description                                   |
|-------------------------|-----------------------------------------------|
| `DjangoFilterBackend`   | Used for filtering queries, like active/inactive friend requests. |

## Tasks

| Task                             | Description                                                         |
|----------------------------------|---------------------------------------------------------------------|
| `delete_expired_friend_requests` | Celery task for deleting friend requests older than 90 days.        |
