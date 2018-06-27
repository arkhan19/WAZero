from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.

def reminder(request):
    return render(request, template_name='Reminders/reminder.html')