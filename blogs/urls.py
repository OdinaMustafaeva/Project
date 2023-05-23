from django.urls import path

from blogs.views import BlogListCreateView, BlogDetailView, BlogLikeDislikeView, BlogCommentView

urlpatterns = [
    path("", BlogListCreateView.as_view(), name="blog_list_create"),
    path("<slug:slug>/comments/", BlogCommentView.as_view(), name="blog_detail"),
    path("<slug:slug>/like_dislike/", BlogLikeDislikeView.as_view(), name="blog_like_dislike"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
