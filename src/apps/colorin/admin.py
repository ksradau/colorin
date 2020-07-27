from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.colorin.models import InstagramProfile


@admin.register(InstagramProfile)
class ColorinAdminModel(ModelAdmin):
    pass
