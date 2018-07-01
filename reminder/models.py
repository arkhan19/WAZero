# from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.conf import settings


class Reminder(models.Model):
    """
    The most important object for this application.
    Allows users to create and edit reminders that they
    need to complete. They can set names, descriptions,
    and due dates.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='SET_NULL') # Reminder's Owner, for mixins.py

    title = models.CharField(max_length=100, null=False)  # Reminder's Title
    description = models.TextField(blank=True)  # Text Field of Reminder Descriptiom
    due_date = models.DateField(blank=True, null=True)  # For Keeping Due Date of Reminder
    complete_time = models.DateTimeField(blank=True, null=True)  # For Checkign Completition of Reminder

    @property
    def is_complete(self):
        """
        Checks if a Reminder is complete on a Date.
        :return: True if Reminder has been completed as indicated by a truthy
        value for complete_time. Otherwise, False.
        """
        return self.complete_time and self.complete_time < timezone.now()

    @property
    def due_soon(self):
        """
        Checks if a Reminder is due soon.
        :return: True if Reminder is due within two day. Otherwise, False.
        """
        min_due = timezone.now() + timezone.timedelta(days=2)
        return bool(
            self.due_date and self.due_date < min_due)

    def mark_complete(self, commit=True):
        """
        Marks a Reminder as complete by storing the current UTC time in complete_time
        """
        self.complete_time = timezone.now()
        if commit:
            self.save()

    def mark_incomplete(self, commit=True):
        """
        Marks a Reminder as incomplete by storing None in complete_time
        """
        self.complete_time = None
        if commit:
            self.save()
