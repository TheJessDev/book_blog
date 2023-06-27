from django.urls import path
from posts import views


urlpatterns = [
    path("new/", views.PostCreateView.as_view(), name='new'),
    path("", views.PostListView.as_view(), name = 'list'),
]


