from django.urls import path

from categories.views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("", CategoryListCreateView.as_view(), name="categories-list-create"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="category-detail")
]
