from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.colorin.models import ColorinModel


@admin.register(ColorinModel)
class ColorinAdminModel(ModelAdmin):
    pass
