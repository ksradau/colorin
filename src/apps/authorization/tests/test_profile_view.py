from django.test import TestCase

from apps.authorization.views.profile import ProfileView
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/o/me/",
            expected_view_name="authorization:me",
            expected_view=ProfileView,
            expected_template="authorization/me.html",
        )
