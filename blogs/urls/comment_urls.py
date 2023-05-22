from django.urls import path

from blogs.views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path("", CommentListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/", CommentDetailView.as_view(), name="blog_detail"),
]
