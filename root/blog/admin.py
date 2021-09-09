"""Blog models admin."""

from django.contrib import admin

# Models
from root.blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category model admin"""

    list_display = ["name"]
    search_fields = [
        "name",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile model admin"""

    list_display = [
        "user",
        "categories",
        "title",
        "intro",
        "body",
        "image_header",
        "is_draft",
        "url",
        "publish_date",
    ]
    search_fields = [
        "user",
        "categories",
        "title",
        "publish_date",
    ]
