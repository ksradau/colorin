from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.authorization.views import SignInView
from apps.authorization.views.profile import ProfileView
from project.utils.user_utils import UserTestMixin
from project.utils.validate_response import TemplateResponseTestMixin

User = get_user_model()


class Test(TestCase, TemplateResponseTestMixin, UserTestMixin):
    def test_sign_in_get(self):
        self.validate_response(
            url=f"/o/sign_in/",
            expected_view_name="authorization:sign_in",
            expected_template="authorization/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_sign_in_post_success(self):
        user = self.create_user()

        form_data = {
            "username": user.username,
            "email": user.email,
            "password": user.username,
        }

        self.validate_response(
            url=f"/o/sign_in/",
            method="post",
            form_data=form_data,
            expected_view_name="authorization:me",
            expected_template="authorization/me.html",
            expected_view=ProfileView,
            expected_redirect_chain=[("/o/me/", 302)],
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_sign_in_post_failure_bad_creds(self):
        user = self.create_user()

        form_data = {
            "username": user.username,
            "email": user.email,
            "password": user.username * 2,
        }

        self.validate_response(
            url=f"/o/sign_in/",
            method="post",
            form_data=form_data,
            expected_view_name="authorization:sign_in",
            expected_template="authorization/sign_in.html",
            expected_view=SignInView,
            content_filters=(lambda _c: b"error" in _c,),
        )

    def test_signin_verified_success(self):
        user = self.create_user(verified=True)

        self.validate_response(
            url=f"/o/sign_in/{user.username}/",
            expected_view_name="authorization:me",
            expected_template="authorization/me.html",
            expected_view=ProfileView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
            expected_redirect_chain=[("/o/me/?newbie=1", 302)],
        )

    def test_signin_verified_failure_bad_code(self):
        user = self.create_user(verified=True)

        self.validate_response(
            url=f"/o/sign_in/{user.username * 2}/",
            expected_view_name="authorization:sign_in",
            expected_template="authorization/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )

    def test_signin_verified_failure_not_verified(self):
        user = self.create_user()

        self.validate_response(
            url=f"/o/sign_in/{user.username}/",
            expected_view_name="authorization:sign_in",
            expected_template="authorization/sign_in.html",
            expected_view=SignInView,
            content_filters=(
                lambda _c: b"error" not in _c,
                lambda _c: b"Error" not in _c,
            ),
        )
