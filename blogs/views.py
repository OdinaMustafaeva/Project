from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.serializers.blog import BlogLikeDislikeSerializer, BlogCommentSerializer
from paginations import CustomPageNumberPagination
from blogs.models import Blog, LikeDislike, Comment
from blogs.serializers import BlogSerializer, BlogCreateSerializer


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category", "author__email")
    ordering_fields = ("id", "slug")
    search_fields = ("title", "category__title")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BlogCreateSerializer
        return BlogSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return BlogCreateSerializer
        return BlogSerializer


class BlogLikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BlogLikeDislikeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = BlogLikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        type_ = serializer.validated_data.get("type")
        user = request.user
        blog = Blog.objects.filter(slug=self.kwargs.get("slug")).first()
        if not blog:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(blog=blog, user=user).first()
        if like_dislike_blog and like_dislike_blog.type == type_:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(blog=blog, user=user, defaults={"type": type_})
        data = {"type": type_, "detail": "Liked or disliked."}
        return Response(data)


class BlogCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(slug=self.kwargs.get("slug")).first()
        data_comments = Comment.objects.filter(blog=blog)
        serializer = BlogCommentSerializer(data_comments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BlogCommentSerializer)
    def post(self, request, *args, **kwargs):
        serializer = BlogCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        body = serializer.validated_data.get("body")
        user = request.user
        blog = Blog.objects.filter(slug=self.kwargs.get("slug")).first()
        if not blog:
            raise Http404
        Comment.objects.update_or_create(blog=blog, user=user, body=body)
        data = {"blog": blog}
        return Response(data)


