from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.colorin.models import ColorinPage


@admin.register(ColorinPage)
class ColorinPageAdminModel(ModelAdmin):
    pass
