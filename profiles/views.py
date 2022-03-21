from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponseRedirect


# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template = 'registration/register.html'
    success_url = reverse_lazy('home')

def login(request):
    return render(request, 'login.html', {})

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')