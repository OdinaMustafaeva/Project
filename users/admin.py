from django.contrib import admin

from .models import User, VerificationCode


@admin.register(User)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "gender"]


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ["email", "code", "last_sent_time", "expired_at", "is_verified"]
    ordering = ["-last_sent_time"]
