from django.urls import path

from apps.authorization.apps import AuthConfig
from apps.authorization.views import IndexView
from apps.authorization.views import PwcDoneView
from apps.authorization.views import PwcView
from apps.authorization.views import SignInVerifiedView
from apps.authorization.views import SignInView
from apps.authorization.views import SignOutView
from apps.authorization.views import SignUpConfirmedView
from apps.authorization.views import SignUpView
from apps.authorization.views.profile import ProfileView
from apps.authorization.views.profile_edit import ProfileEditView

app_name = AuthConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("me/", ProfileView.as_view(), name="me"),
    path("me/edit/", ProfileEditView.as_view(), name="me_edit"),
    path("pwc/", PwcView.as_view(), name="pwc"),
    path("pwc/done/", PwcDoneView.as_view(), name="pwc_done",),
    path("sign_in/", SignInView.as_view(), name="sign_in",),
    path("sign_in/<str:code>/", SignInVerifiedView.as_view(), name="sign_in_verified",),
    path("sign_out/", SignOutView.as_view(), name="sign_out",),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("sign_up/confirmed/", SignUpConfirmedView.as_view(), name="sign_up_confirmed"),
]
