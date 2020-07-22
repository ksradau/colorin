from django.urls import path

from apps.colorin.apps import ColorinConfig
from apps.colorin.views import IndexView, AddPhotoView, AllPhotoView

app_name = ColorinConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("all/", AllPhotoView.as_view(), name="colorin-all"),
    path("add/", AddPhotoView.as_view(), name="colorin-add"),
]
