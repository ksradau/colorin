from os import urandom

from django.test import TestCase

from apps.resume.models import Project
from apps.resume.models import Responsibility
from apps.resume.models import ResumePage
from apps.resume.models import Technology
from apps.resume.views import IndexView
from project.utils.validate_response import TemplateResponseTestMixin


class Test(TestCase, TemplateResponseTestMixin):
    def test_project(self):
        placeholder = urandom(4).hex()

        # resp = Responsibility(summary=placeholder)

        pj = Project(name=placeholder)
        self.assertEqual(str(pj), f"{placeholder} [id_{pj.pk}]")

    def test_responsibility(self):
        placeholder = urandom(4).hex()

        responsibility = Responsibility(summary=placeholder)
        self.assertEqual(
            str(responsibility), f"Responsibility [id_{responsibility.pk}]"
        )

    def test_technology(self):
        placeholder = urandom(4).hex()

        technology = Technology(name=placeholder)
        self.assertEqual(str(technology), f"{placeholder} [id_{technology.pk}]")

    def test_resumepage(self):
        placeholder = urandom(4).hex()
        resumepage = ResumePage(h1=placeholder)
        self.assertEqual(str(resumepage), f"ResumePage [id_{resumepage.pk}]")

    def test_get(self):
        self.validate_response(
            url="/resume/",
            expected_view=IndexView,
            expected_view_name="resume:index",
            expected_template="resume/index.html",
        )
