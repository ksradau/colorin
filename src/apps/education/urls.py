from django.urls import path

from apps.education.apps import EducationConfig
from apps.education.views import IndexView

app_name = EducationConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
