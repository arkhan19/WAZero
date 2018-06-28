from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from .models import Reminder
from .forms import ReminderForm
from .mixins import SuccessReminderListMixin, ReminderOwnedByUserMixin


class ReminderListView(TemplateView):
    """
    View to view tasks. Views tasks for current logged in user
    """
    template_name = 'Reminders/reminder_list.html'

    def get_queryset(self):
        return Reminder.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReminderListView, self).get_context_data(**kwargs)
        context['reminder'] = self.get_queryset()
        return context

    # Template_name = 'Reminders/reminder_list.html'


class NewReminderView(SuccessReminderListMixin, CreateView):
    """
    View to create a task. Owner is set upon validation.
    Goes to reminder list upon completion.
    """
    template_name = 'Reminders/reminder.html'
    form_class = ReminderForm

    def form_valid(self, form):
        reminder = form.save(commit=False)
        reminder.owner = self.request.user
        reminder.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteReminderView(ReminderOwnedByUserMixin, SuccessReminderListMixin, DeleteView):
    """
    View to delete a Reminder. Must be owner to delete a Reminder. Redirect
    to Reminder list upon completion.
    """
    model = Reminder
    pk_url_kwarg = 'reminder_id'


class ReminderView(ReminderOwnedByUserMixin, SuccessReminderListMixin, UpdateView):
    """
    View to view and edit a Reminder. Must be owner to edit a Reminder. Redirect
    to Reminder list upon completion.
    """
    template_name = 'Reminders/reminder.html'
    form_class = ReminderForm
    pk_url_kwarg = 'reminder_id'

    def get_queryset(self):
        if hasattr(self.request, 'user') and self.request.user.is_active:
            return Reminder.objects.filter(owner=self.request.user)
        return Reminder.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(ReminderView, self).get_context_data(**kwargs)
        context['update'] = True
        return context


def toggle_complete_view(request, reminder_id):
    """
    Toggles complete state of task. If Reminder with id reminder_id is
    incomplete, mark as complete. Else, mark as incomplete.
    Only the Reminder owner can modify the Reminder.
    """
    try:
        reminder = Reminder.objects.get(pk=reminder_id, owner=request.user)
    except Reminder.DoesNotExist:
        return HttpResponseNotFound()

    # Reminder object created above will be used now
    if reminder.is_complete:
        reminder.mark_incomplete()
    else:
        reminder.mark_complete()
    # from django.urls import reverse
    return HttpResponseRedirect(reverse('reminder'))

