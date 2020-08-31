from django.urls import path

from apps.colorin.apps import ColorinConfig
from apps.colorin.views import IndexView, AllPhotoView, FileFieldView
from apps.colorin.views import download_zip, update_info, update_info_first, match_images, add_emoji_to_db, match_emoji_pics

app_name = ColorinConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("all/", AllPhotoView.as_view(), name="colorin-all"),
    path("add/", FileFieldView.as_view(), name="file_field"),
    path("download/", download_zip, name="download"),
    path("update/", update_info, name="update"),
    path("first-update/", update_info_first, name="update-first"),
    path("match/", match_images, name="match"),
    path("add-emoji/", add_emoji_to_db, name="add-emoji"),
    path("match-emoji/", match_emoji_pics, name="match-emoji"),
]
