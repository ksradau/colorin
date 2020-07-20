from os import urandom
from unittest import skip

from django.test import TestCase

from apps.education.models import EducationPage
from apps.education.views import IndexView
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/education/",
            expected_view_name="education:index",
            expected_view=IndexView,
            expected_template="education/index.html",
        )

    def test_edupage(self):
        placeholder = urandom(4).hex()
        edupage = EducationPage(title=placeholder)
        self.assertEqual(str(edupage), f"EducationPage(id={edupage.pk})")
