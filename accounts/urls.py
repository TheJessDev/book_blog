from django.urls import path
from .views import SignupView, PasswordChangeView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('password_change/', PasswordChangeView.as_view(), name= 'password_change'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("profile/edit", ProfileUpdateView.as_view(), name='profile_update'),

]