from django.test import TestCase

from apps.authorization.models import AuthProfile
from periodic.utils.xmodels import get_auth_profile_model


class Test(TestCase):
    def test_get_auth_profile_model(self):
        model = get_auth_profile_model()
        self.assertIs(model, AuthProfile)
