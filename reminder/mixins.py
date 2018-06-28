from django.shortcuts import get_object_or_404
from .models import Reminder


class SuccessReminderListMixin(object):
    """
    Uses lazy imported reverse to resolve success URL
    for views that redirect to object view.
    Note: This is not absolutely necessary, as reversible
    name can be used in success_url attribute for most classes.
    """
    def get_success_url(self):
        from django.urls import reverse
        return reverse('reminder')


class ReminderOwnedByUserMixin(object):
    """
    For methods that manipulate reminder via POST, a mixin that
    ensures the current logged in user owns the specified reminder.
    If not, return a 404 instead of a 403 to obfuscate the existence
    of that object.
    """
    def post(self, request, reminder_id=None, *args, **kwargs):
        if reminder_id:
            # Validate that user owns task or 404
            get_object_or_404(Reminder, pk=reminder_id, owner=request.user)
        return super(ReminderOwnedByUserMixin, self).post(request, *args, **kwargs)