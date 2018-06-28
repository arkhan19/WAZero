from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):
    """
    A model form for a Reminder object.
    Each Reminder will have this form, ie., these items will be views from reminder object
    exclude consist of all the attributes of reminder object which will be exluded from reminder view.
    """
    class Meta:
        exclude = ['pk', 'owner', 'complete_time']
        model = Reminder
        """
        model consists of Reminder model now.
        """
