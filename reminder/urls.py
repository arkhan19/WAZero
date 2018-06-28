# from django.urls import path
# from reminder import views as reminder_views
# from django.contrib.auth.decorators import login_required
#
# app_name = 'reminder'
# urlpatterns = [
#     path('', login_required(reminder_views.ReminderListView.as_view(template_name='Reminders/test.html'), login_url='login'),
#          name='reminder'),
#     path('', login_required(reminder_views.NewReminderView.as_view()), name='reminder-add'),
#     path('<slug:remainder_id>', login_required(reminder_views.ReminderView.as_view()), name='reminder-edit'),
#
#
#
#
#     # path(r'^reminder/$', login_required(reminder_views.ReminderListView.as_view(), login_url='login'), name='reminders'),
#     # path(r'^reminder/(?P<reminder_id>\d+)/$', login_required(reminder_views.ReminderView.as_view()), name='reminder-edit'),
#     # path(r'^delete/(?P<reminder_id>\d+)/$', login_required(reminder_views.DeleteReminderView.as_view()), name='reminder-delete'),
#     # path(r'^toggle/(?P<reminder_id>\d+)/$', login_required(reminder_views.toggle_complete_view), name='reminder-toggle'),
#
# ]
