from django.db import models as m
from django.contrib.auth import get_user_model
import uuid
from storages.backends.s3boto3 import S3Boto3Storage

User = get_user_model()


class InstagramProfile(m.Model):
    user = m.OneToOneField(
        User, on_delete=m.CASCADE, primary_key=True, related_name="instagram_profile"
    )
    inst_profile_pic = m.FileField(storage=S3Boto3Storage())
    inst_profile_pic_url = m.TextField(null=True, blank=True)
    inst_full_name = m.TextField(null=True, blank=True)
    inst_biography = m.TextField(null=True, blank=True)
    inst_theme_color = m.TextField(null=True, blank=True)
    emoji_match_list = m.TextField(null=True, blank=True)


class InstagramPhoto(m.Model):
    uuid = m.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = m.ForeignKey(InstagramProfile, on_delete=m.CASCADE, related_name="instagram_photos")
    photo = m.FileField(storage=S3Boto3Storage())
    photo_url = m.TextField(null=True, blank=True)
    palette = m.TextField(null=True, blank=True)
    dominant = m.TextField(null=True, blank=True)
    similar = m.TextField(null=True, blank=True)


class UploadedPhoto(m.Model):
    uuid = m.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name="uploaded_photos")
    photo = m.FileField(storage=S3Boto3Storage())
    is_match = m.BooleanField(null=True, blank=True)
    palette = m.TextField(null=True, blank=True)
    dominant = m.TextField(null=True, blank=True)


class EmojiPic(m.Model):
    emoji_name = m.TextField(null=True, blank=True)
    palette = m.TextField(null=True, blank=True)
