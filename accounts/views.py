from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.views.generic import DetailView, UpdateView, TemplateView

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('list')
    template_name = 'registration/profile_update.html'

    def get_object(self, queryset=None):
        return self.request.user 

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_password'] = False  # Remove the password message
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class ProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user 


class PasswordChangeFormPageView(FormView):
    template_name = 'registration/password_change_form.html'

class PasswordChangeDonePageView(TemplateView):
    template_name = 'registration/password_change_done.html'

