from django.urls import path

from apps.colorin.apps import ColorinConfig
from apps.colorin.views import IndexView, AllPhotoView, FileFieldView, download_zip

app_name = ColorinConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("all/", AllPhotoView.as_view(), name="colorin-all"),
    path("add/", FileFieldView.as_view(), name="file_field"),
    path("download/", download_zip(), name="download"),
    path("update/", update_info(), name="update"),
]
