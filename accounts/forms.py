from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser
from django.forms import ModelForm 


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']


class CustomUserChangeForm(ModelForm):
    class Meta(ModelForm):
        model = CustomUser
        fields = ['bio', 'profile_image', 'username', 'email']
        exclude=['password1', 'password2']
