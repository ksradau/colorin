from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.urls import path

from apps.authorization.views import SignUpView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change_form/", PasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change_done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("registration/", SignUpView.as_view(), name="signup"),
]