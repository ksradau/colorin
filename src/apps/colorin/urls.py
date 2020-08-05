from django.urls import path

from apps.colorin.apps import ColorinConfig
from apps.colorin.views import IndexView, AllPhotoView, FileFieldView

app_name = ColorinConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("all/", AllPhotoView.as_view(), name="colorin-all"),
    path("add/", FileFieldView.as_view(), name="file_field")
]
