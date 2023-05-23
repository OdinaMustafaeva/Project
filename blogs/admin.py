from django.contrib import admin
from blogs.models import Blog, LikeDislike, Comment


# Register your models here.


@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "category"]


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ["user", "blog", "type"]


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "blog", "body"]
