from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from paginations import CustomPageNumberPagination
from blogs.models import Blog
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
