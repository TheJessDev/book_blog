from django.urls import path
from .views import SignupView, PasswordChangeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('password_change/', PasswordChangeView.as_view(), name= 'password_change'),
]