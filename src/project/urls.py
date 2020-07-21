from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

STATIC_DIR = settings.PROJECT_DIR / "static"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.index.urls")),
    path("colorin/", include("apps.colorin.urls")),
    path("try-colorin/", include("apps.try-colorin.urls")),
    path("auth/", include("apps.authorization.urls")),
]
