"""WAZero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import Home, register, index
from django.contrib.auth.decorators import login_required
from reminder import views as reminder_views

urlpatterns = [


    # Basic Home Path

    path('', Home.as_view(), name='home'),
    path('index/', index, name='index'),


    # Authorisation

    path('login/', auth_views.login, name='login'),
    path('logout/', Home.logout_view, name='logout'),
    path('register/', register, name='register'),


    # Reminders

    path('reminders/', login_required(reminder_views.ReminderListView.as_view(), login_url='login'), name='reminder'),
    path('reminder/', login_required(reminder_views.NewReminderView.as_view()), name='add'),
    path('reminder/<int:reminder_id>/', login_required(reminder_views.ReminderView.as_view()), name='edit'),
    path('delete/<int:reminder_id>/', login_required(reminder_views.DeleteReminderView.as_view()), name='delete'),
    path('toggle/<int:reminder_id>/', login_required(reminder_views.toggle_complete_view), name='toggle'),


    # Admin

    path('admin/', admin.site.urls),

]
