from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
# from roles.models import ClinicUserManager
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# LoginRequiredMixin é uma condição pra so fazer o que quer se estiver logado antes

from django.urls import reverse_lazy
# from roles.forms import ClinicUserCreationForm

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/logar.html'
    success_url = reverse_lazy('core:index')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass 
