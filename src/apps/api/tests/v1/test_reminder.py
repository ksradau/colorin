from datetime import timedelta
from os import urandom

from django.test import TestCase
from rest_framework import status

from applications.reminders.models import Reminder
from applications.reminders.utils.consts import ReminderStatus
from project.utils.xdatetime import near
from project.utils.xdatetime import utcnow
from project.utils.xtests import ApiTestMixin
from project.utils.xtests import UserTestMixin


class Test(TestCase, ApiTestMixin, UserTestMixin):
    def setUp(self) -> None:
        self.endpoint = "/api/v1/reminder/"
        self.user = self.create_user()
        self.token = self.create_auth_token(self.user)
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Token {self.token}"}

        self.user2 = self.create_user()
        self.reminder2 = Reminder(creator=self.user2)
        self.reminder2.save()

    def test_user_get_anon(self):
        self.validate_response(
            self.endpoint, expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_user_normal(self):
        reminder = Reminder(creator=self.user)
        reminder.save()

        self.validate_response(
            self.endpoint,
            headers=self.auth_headers,
            expected_response_payload=[
                {
                    "created_at": reminder.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    "creator": self.user.pk,
                    "description": reminder.description,
                    "id": reminder.pk,
                    "location": reminder.location,
                    "notified_at": reminder.notified_at,
                    "notify_at": reminder.notify_at,
                    "participants": [],
                    "status": ReminderStatus.CREATED.name,
                    "title": reminder.title,
                },
            ],
        )

    def test_post_anon(self):
        self.validate_response(
            self.endpoint,
            method="post",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_post_normal(self):
        placeholder = urandom(4).hex()
        title = f"title_{placeholder}"

        self.validate_response(
            self.endpoint,
            method="post",
            headers=self.auth_headers,
            data={"title": title,},
            expected_status_code=status.HTTP_201_CREATED,
        )

        reminders = Reminder.objects.filter(title=title)
        self.assertEqual(1, reminders.count())

        reminder = reminders.first()
        self.assertTrue(reminder)

        self.assertEqual(title, reminder.title)
        self.assertEqual(self.user, reminder.creator)
        self.assertTrue(near(utcnow(), reminder.created_at, 4))
        self.assertTrue(ReminderStatus.CREATED.name, reminder.status)

    def test_patch_anon(self):
        reminder = Reminder(creator=self.user)
        reminder.save()

        self.validate_response(
            f"{self.endpoint}{reminder.pk}/",
            method="patch",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_patch_normal_title(self):
        rem = Reminder(creator=self.user, title="xxx")
        rem.save()

        self.validate_response(
            f"{self.endpoint}{rem.pk}/",
            method="patch",
            headers=self.auth_headers,
            data={"title": "yyy",},
            expected_status_code=status.HTTP_200_OK,
        )

        reminders = Reminder.objects.filter(title="yyy")
        self.assertEqual(1, reminders.count())

        reminder = reminders.first()
        self.assertTrue(reminder)

        self.assertEqual("yyy", reminder.title)
        self.assertEqual(rem.creator, reminder.creator)
        self.assertListEqual(
            list(rem.participants.all()), list(reminder.participants.all())
        )
        self.assertEqual(rem.pk, reminder.pk)

    def test_patch_normal_readonly(self):
        reminder = Reminder(creator=self.user)
        reminder.save()

        dtm = utcnow() - timedelta(days=1)

        dataset = {
            "created_at": dtm,
            "creator": self.user2.pk,
            "notified_at": dtm,
        }

        old = {_f: getattr(reminder, _f) for _f in dataset}

        for field, value in dataset.items():
            self.validate_response(
                f"{self.endpoint}{reminder.pk}/",
                method="patch",
                headers=self.auth_headers,
                data={field: value},
                expected_status_code=status.HTTP_200_OK,
            )

        reminder.refresh_from_db()

        for field, expected_value in old.items():
            self.assertEqual(expected_value, getattr(reminder, field), field)

    def test_patch_status(self):
        reminder = Reminder(creator=self.user)
        reminder.save()

        self.validate_response(
            f"{self.endpoint}{reminder.pk}/",
            method="patch",
            headers=self.auth_headers,
            data={"status": ReminderStatus.NOTIFIED.name},
            expected_status_code=status.HTTP_400_BAD_REQUEST,
        )

        reminder.refresh_from_db()
        self.assertEqual("CREATED", reminder.status)

        self.validate_response(
            f"{self.endpoint}{reminder.pk}/",
            method="patch",
            headers=self.auth_headers,
            data={"status": ReminderStatus.DONE.name},
            expected_status_code=status.HTTP_200_OK,
        )

        reminder.refresh_from_db()
        self.assertEqual("DONE", reminder.status)

    def test_patch_not_own(self):
        self.validate_response(
            f"{self.endpoint}{self.reminder2.pk}/",
            method="patch",
            headers=self.auth_headers,
            data={"title": "xxx"},
            expected_status_code=status.HTTP_404_NOT_FOUND,
        )

    def test_delete_anon(self):
        self.validate_response(
            f"{self.endpoint}{self.reminder2.pk}/",
            method="delete",
            expected_status_code=status.HTTP_401_UNAUTHORIZED,
        )

    def test_delete_normal(self):
        reminder = Reminder(creator=self.user)
        reminder.save()

        self.validate_response(
            f"{self.endpoint}{reminder.pk}/",
            method="delete",
            headers=self.auth_headers,
            expected_status_code=status.HTTP_204_NO_CONTENT,
        )

        with self.assertRaises(Reminder.DoesNotExist):
            reminder.refresh_from_db()
