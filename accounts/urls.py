from django.urls import path
from .views import (
    SignupView, 
    PasswordChangeFormPageView, 
    ProfileView, 
    ProfileUpdateView, 
    PasswordChangeDonePageView, 
    )

urlpatterns = [
    path('signup/', SignupView.as_view(), name= 'signup'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("profile/edit", ProfileUpdateView.as_view(), name='profile_update'),
    path('password_change/', PasswordChangeFormPageView.as_view(), name= 'password_change'),
    path('password_change_done/', PasswordChangeDonePageView.as_view(), name='password_change_done'),
]