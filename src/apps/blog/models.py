from django.contrib.auth import get_user_model
from django.db import models as m
from django.urls import reverse_lazy

import uuid
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class BlogPost(m.Model):
    title = m.TextField(null=True, blank=True)
    preview = m.TextField(null=True, blank=True)
    content = m.TextField(null=True, blank=True)
    author = m.ForeignKey(User, on_delete=m.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": str(self.pk)})


class Comment(m.Model):
    author = m.ForeignKey(User, on_delete=m.CASCADE)
    post = m.ForeignKey(BlogPost, on_delete=m.CASCADE, related_name="comments")
    nr_likes = m.IntegerField(null=True, blank=True)
    nr_dislikes = m.IntegerField(null=True, blank=True)

    message = m.TextField()


class Photo(m.Model):
    uuid = m.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = m.ForeignKey(BlogPost, on_delete=m.CASCADE, related_name="photos")
    original = m.FileField(storage=S3Boto3Storage())
    thumbnail = m.FileField(storage=S3Boto3Storage(), null=True, blank=True)
