from unittest import TestCase
from reminder.mixins import SuccessReminderListMixin
from django.urls import reverse


class SuccessReminderListMixinTestCase(TestCase):
    def setUp(self):  # CamelCase for Setup is important.
        class Exp(SuccessReminderListMixin):
            pass
        self.case = Exp()

    def test_get_sucess_url(self):
        case_url = reverse('reminder')
        result = self.case.get_success_url()

        self.assertEqual(case_url, result)


