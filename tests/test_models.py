from unittest import TestCase
from reminder.models import Reminder
from django.utils import timezone


class ReminderIsComplete(TestCase):
    def test_is_complete_iscompleted(self):
        case = Reminder()
        case.complete_time = timezone.now() - timezone.timedelta(days=1)

        self.assertTrue(case.is_complete)

    def test_is_complete_isincomplete(self):
        case = Reminder()
        case.complete_time = None

        self.assertFalse(case.is_complete)

    def test_is_complete_infuture(self):
        case = Reminder()
        case.complete_time = timezone.now() + timezone.timedelta(days=1)

        self.assertFalse(case.is_complete)


class ReminderDueSoon(TestCase):
    def test_due_soon(self):
        case = Reminder()
        case.due_date = timezone.now()+timezone.timedelta(days=2)

        self.assertTrue(case.due_soon)

    def test_due_soon_NotDueSoon(self):
        case = Reminder()
        case.due_date = timezone.now()+timezone.timedelta(days = 10)

        self.assertFalse(case.due_soon)

    def test_due_soon_error(self):
        case = Reminder()
        case.due_date = None

        self.assertFalse(case.due_soon)


class ReminderMark(TestCase):
    def test_mark_complete(self):
        case = Reminder()
        case.complete_time = None
        self.assertFalse(case.is_complete)

        case.mark_complete(commit=False)
        self.assertTrue(case.is_complete)

    def test_mark_incomplete(self):
        case = Reminder()
        case.complete_time = timezone.now()
        self.assertTrue(case.is_complete)

        case.mark_incomplete(commit=False)
        self.assertFalse(case.is_complete)
