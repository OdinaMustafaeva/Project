from django.contrib import admin
from categories.models import Category


# Register your models here.

@admin.register(Category)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "position"]
