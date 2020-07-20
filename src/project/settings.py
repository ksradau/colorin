from os import getenv
from pathlib import Path

import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as _settings

PROJECT_DIR = Path(__file__).parent.resolve()  # project url
BASE_DIR = PROJECT_DIR.parent.resolve()  # src url
REPO_DIR = BASE_DIR.parent.resolve()  # repository url


SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS + INTERNAL_IPS + ["localhost"] + ["2b5fd89964c5.ngrok.io"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "apps.authorization.apps.AuthConfig",
    "apps.index",
    "apps.resume",
    "apps.education",
    "apps.blog.apps.BlogConfig",
    "rest_framework",
    "apps.api",
    "rest_framework.authtoken",
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        # тут рендер ищет имена
        "DIRS": [PROJECT_DIR / "jinja2",],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "project.utils.jinja2env.build_jinja2_environment",
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(_db_url, conn_max_age=600),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = [
    PROJECT_DIR / "static",  # где джанге брать статику
    # apps/index.static
]

STATIC_ROOT = (
    REPO_DIR / ".static"
)  # куда соберется вся статика после команды collectstatic - папка создается. типа в джанге куча статики в разных местах и разных приложениях,

STATIC_URL = "/static/"  # путь от которого все отсчитывается на разных сервисах

# LOGIN_URL = reverse_lazy("onboarding:sign_in")
# LOGIN_REDIRECT_URL = reverse_lazy("blog:all_posts")

LOGIN_URL = reverse_lazy("authorization:sign_in")
LOGIN_REDIRECT_URL = reverse_lazy("authorization:me")

SITE_ID = _settings.SITE_ID

EMAIL_HOST = _settings.EMAIL_HOST
EMAIL_HOST_PASSWORD = _settings.EMAIL_HOST_PASSWORD
EMAIL_HOST_USER = _settings.EMAIL_HOST_USER
EMAIL_PORT = _settings.EMAIL_PORT
EMAIL_USE_SSL = _settings.EMAIL_USE_SSL
EMAIL_USE_TLS = _settings.EMAIL_USE_TLS

EMAIL_FROM = _settings.EMAIL_FROM



#ENVVAR_PREFIX_FOR_DYNACONF=SD  если удалить то префикс будет DYNACONF   профайлинг
# set DY=1 make run


AWS_ACCESS_KEY_ID = _settings.AWS_ACCESS_KEY_ID
AWS_DEFAULT_ACL = "public-read"
AWS_LOCATION = _settings.AWS_LOCATION
AWS_QUERYSTRING_AUTH = False
AWS_S3_ADDRESSING_STYLE = "path"
AWS_S3_REGION_NAME = _settings.AWS_S3_REGION_NAME
AWS_SECRET_ACCESS_KEY = _settings.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = "resizeksbucket"
#add to secrets

CELERY_BEAT_SMILE = _settings.CELERY_BEAT_SMILE
TG = _settings.TG
TG_MATRIX = _settings.TG_MATRIX
