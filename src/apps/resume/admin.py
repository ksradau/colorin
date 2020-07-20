from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Project
from apps.resume.models import Responsibility
from apps.resume.models import ResumePage
from apps.resume.models import Technology
from project.utils.forms import gen_textinput_admin_form


@admin.register(ResumePage)
class ResumePageAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        ResumePage, (ResumePage.title, ResumePage.h1, ResumePage.preview)
    )


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Technology, (Technology.name, Technology.description)
    )


@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(Project, (Project.link, Project.name))


@admin.register(Responsibility)
class ResponsibilityAdminModel(ModelAdmin):
    pass
