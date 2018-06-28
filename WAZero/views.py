from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import RedirectView

class Home(RedirectView):
    #return render(request, template_name='registration/signin.html')
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        if hasattr(self.request, 'user') and self.request.user.is_active:
            return reverse('reminder')
        else:
            return reverse('login')

    def logout_view(request):
        logout(request)
        return redirect('login')

def index (request):
    return render(request, 'index.html')

def register(request):
    """
    Registration view. Registers a new user using Django's
    built in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })