from django.urls import path

from blogs.views import LikeDislikeListCreateView, LikeDislikeDetailView

urlpatterns = [
    path("", LikeDislikeListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/", LikeDislikeDetailView.as_view(), name="blog_detail"),
]
