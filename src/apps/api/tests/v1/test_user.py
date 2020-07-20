from django.test import TestCase
from rest_framework import status

from project.utils.xtests import ApiTestMixin
from project.utils.xtests import UserTestMixin


class Test(TestCase, ApiTestMixin, UserTestMixin):
    def setUp(self) -> None:
        self.endpoint = "/api/v1/user/"
        self.user = self.create_user()
        self.token = self.create_auth_token(self.user)
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

    def test_user_get_anon(self):
        self.validate_response(
            self.endpoint, expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_user_normal(self):
        self.validate_response(
            self.endpoint,
            headers=self.auth_headers,
            expected_response_payload=[{"id": self.user.pk, "email": self.user.email,}],
        )

    def test_post_anon(self):
        self.validate_response(
            self.endpoint,
            method="post",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_post_normal(self):
        self.validate_response(
            self.endpoint,
            method="post",
            headers=self.auth_headers,
            expected_status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_patch_anon(self):
        self.validate_response(
            f"{self.endpoint}{self.user.pk}/",
            method="patch",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_patch_normal(self):
        self.validate_response(
            f"{self.endpoint}{self.user.pk}/",
            method="patch",
            headers=self.auth_headers,
            expected_status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_delete_anon(self):
        self.validate_response(
            f"{self.endpoint}{self.user.pk}/",
            method="delete",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_delete_normal(self):
        self.validate_response(
            f"{self.endpoint}{self.user.pk}/",
            method="delete",
            headers=self.auth_headers,
            expected_status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
