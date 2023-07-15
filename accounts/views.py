from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registrations/signup.html'


class PasswordChangeView(FormView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_change_done')
    #template_name = 'registration/password_change_form.html'