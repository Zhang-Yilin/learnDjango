from django.contrib import admin
from .models import BlogType, Blog, ReadList


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_time", "blog_type")


@admin.register(ReadList)
class ReadListAdmin(admin.ModelAdmin):
    list_display = ("id", "read_time", "read_blog")