from unittest import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):
    def test_server_timezon_unchanged(self):
        target_timezone = 'UTC'
        self.assertEqual(target_timezone, settings.TIME_ZONE)