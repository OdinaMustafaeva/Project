from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from categories.models import Category
from categories.serializers import CategorySerializer
from paginations import CustomPageNumberPagination


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("title", "parent")
    ordering_fields = ("id", "title")
    search_fields = ("title", "position")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CategorySerializer
        return CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CategorySerializer
        return CategorySerializer
