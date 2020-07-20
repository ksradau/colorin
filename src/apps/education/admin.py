from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.education.models import EducationPage


@admin.register(EducationPage)
class EducationPageAdminModel(ModelAdmin):
    pass
