from datetime import datetime
from unittest.mock import MagicMock
from unittest.mock import patch

from delorean import parse
from django.contrib.sites.models import Site
from django.test import TestCase
from freezegun import freeze_time

from apps.authorization.models import AuthProfile
from apps.authorization.utils.verification import start_verification
from periodic import tasks
from project.utils.date import near
from project.utils.date import utcnow
from project.utils.user_utils import UserTestMixin


class Test(UserTestMixin, TestCase):
    @freeze_time("2020-01-01 01:02:03")
    @patch.object(tasks.invite, "send_email")
    def test_invite_single(self, mock_send_email):
        atm = utcnow()

        request = MagicMock()
        request.site = Site.objects.first()

        user_degenerate = self.create_user()
        user_not_verified = self.create_user()
        user_verified = self.create_user(verified=True)

        ap_degenerated = AuthProfile(user=user_degenerate, site=request.site)
        ap_degenerated.save()
        start_verification(request, user_not_verified)
        start_verification(request, user_verified)

        tasks.invite_single_user(user_degenerate.email)
        self.assertFalse(mock_send_email.called)
        ap_degenerated.refresh_from_db()
        self.assertIsNone(ap_degenerated.verified_at)
        self.assertIsNone(ap_degenerated.notified_at)
        self.assertFalse(ap_degenerated.verification_code)

        mock_send_email.reset_mock()
        tasks.invite_single_user(user_not_verified.email)
        ap: AuthProfile = user_not_verified.auth_profile
        mock_send_email.assert_called_once_with(
            context={"link": ap.link, "service": "Ksradau.herokuapp.com"},
            email_to=user_not_verified.email,
            mail_template_name="invitation",
            subject=f"Registration at Ksradau.herokuapp.com",
        )
        ap.refresh_from_db()
        self.assertIsNone(ap.verified_at)
        self.assertTrue(near(atm, ap.notified_at, 1))
        self.assertTrue(ap.link)

        mock_send_email.reset_mock()
        tasks.invite_single_user(user_verified.email)
        ap: AuthProfile = user_verified.auth_profile
        mock_send_email.assert_called_once_with(
            context={"link": ap.link, "service": "Ksradau.herokuapp.com"},
            email_to=user_verified.email,
            mail_template_name="invitation",
            subject=f"Registration at Ksradau.herokuapp.com",
        )
        ap.refresh_from_db()
        self.assertIsNone(ap.verified_at)
        self.assertTrue(near(atm, ap.notified_at, 1))
        self.assertTrue(ap.link)
