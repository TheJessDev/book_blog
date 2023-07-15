from django.urls import path
from posts import views


urlpatterns = [
   # path("login/", views.LoginView.as_view(), name='login'),
    #path("signup/", views.SignupView.as_view(), name='signup'),
    #path("profile/", views.UserProfileUpdateView.as_view(), name='profile'),
    path("new/", views.PostCreateView.as_view(), name='new'),
    path("", views.PostListView.as_view(), name ='list'),
    path("my-list/", views.MyPostListView.as_view(), name ='my_list'),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name ='edit'),
    path("<int:pk>/details", views.PostDetailView.as_view(), name ='details'),
]


# all users are able to view listed posts, but only logged in users can edit/delete

# need a 'read more' link to show full review for all users
# 'read more' then needs to take to a details view
# create detail view and link on list
# logged in users will have option to edit or delete

# login page needs redirect to lists page
# About page will contain contents from Home page, home page link can be removed
# Sign up page and link


