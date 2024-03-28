from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


