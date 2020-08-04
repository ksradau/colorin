# Generated by Django 3.0.8 on 2020-08-04 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='instagram_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('inst_profile_pic', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('inst_login', models.TextField(blank=True, null=True)),
                ('inst_full_name', models.TextField(blank=True, null=True)),
                ('inst_biography', models.TextField(blank=True, null=True)),
                ('inst_theme_color', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedPhoto',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('is_match', models.BooleanField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPhoto',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instagram_photos', to='colorin.InstagramProfile')),
            ],
        ),
    ]
