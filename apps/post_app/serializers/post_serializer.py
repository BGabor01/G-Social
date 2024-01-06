from rest_framework import serializers

from apps.post_app.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['owner', 'text', 'image']
        read_only_fields = ['owner'] 

    def validate(self, data):
        if not data.get('text') and not data.get('image'):
            raise serializers.ValidationError("At least one of 'text' or 'image' must be provided.")

        return data