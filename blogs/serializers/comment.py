from rest_framework import serializers
from blogs.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id", "blog", "user", "body")


class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("id", "blog", "user", "body")
        read_only_fields = ("id",)
