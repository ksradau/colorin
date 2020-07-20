from django.urls import path

from apps.colorin.apps import ColorinConfig
from apps.colorin.views import IndexView

app_name = ColorinConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
