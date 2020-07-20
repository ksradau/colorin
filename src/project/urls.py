from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

STATIC_DIR = settings.PROJECT_DIR / "static"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.index.urls")),
    path("resume/", include("apps.resume.urls")),
    path("education/", include("apps.education.urls")),
    path("blog/", include("apps.blog.urls")),
    path("o/", include("apps.authorization.urls")),
    path("api/", include("apps.api.urls"))
]
