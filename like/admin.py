from django.contrib import admin
from .models import LikeRecord, LikeCount

@admin.register(LikeRecord)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "content_type", "object_id", "user")


@admin.register(LikeCount)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "content_type", "object_id", "count")
