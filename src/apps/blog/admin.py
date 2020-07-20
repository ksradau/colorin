from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.blog.models import BlogPost
from apps.blog.models import Comment
from apps.blog.models import Photo


@admin.register(BlogPost)
class BlogPostAdminModel(ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass
