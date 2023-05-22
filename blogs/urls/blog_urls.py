from django.urls import path

from blogs.views import BlogListCreateView, BlogDetailView

urlpatterns = [
    path("", BlogListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
