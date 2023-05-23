from rest_framework import serializers
from blogs.models import Blog, Comment, LikeDislike
from categories.models import Category
from users.models import User


class BlogAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email")


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer()
    author = BlogAuthorSerializer()

    class Meta:
        model = Blog
        fields = (
        "id", "author", "title", "slug", "image", "category", "collab", "body", "likes", "dislikes", "comment")


class BlogCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    category = BlogCategorySerializer()
    author = BlogAuthorSerializer()

    class Meta:
        model = Blog
        fields = ["id", "author", "title", "slug", "image", "category", "collab", "body"]


class BlogCommentSerializer(serializers.ModelSerializer):
    user = BlogAuthorSerializer()

    class Meta:
        model = Comment
        fields = ("id", "blog", "user", "body")
        read_only_fields = ("id",)


class BlogLikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeType.choices)
