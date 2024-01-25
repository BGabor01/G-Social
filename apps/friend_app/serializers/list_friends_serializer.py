from rest_framework import serializers

from apps.friend_app.models import FriendListModel


class ListFriendsSerializer(serializers.ModelSerializer):
    """
    Serializer for listing friends.

    This serializer is used for retrieving and displaying all fields of the FriendListModel.
    It is typically used to display a user's friend list, including all associated details stored in the FriendListModel.

    Meta:
        - model (FriendListModel): The model associated with this serializer.
        - fields (str): Specifies that all fields of the model should be included in the serialized output.
    """
    class Meta:
        fields = '__all__'
        model = FriendListModel
