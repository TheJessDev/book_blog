from django.urls import path
from posts import views


urlpatterns = [
    path("new/", views.PostCreateView.as_view(), name='new'),
    path("", views.PostListView.as_view(), name = 'list'),
    path("my-list/", views.MyPostListView.as_view(), name = 'my_list'),
    path("edit/<int:pk>/", views.PostUpdateView.as_view(), name = 'edit'),
    path("<int:pk>/details", views.PostDetailView.as_view(), name = 'details'),
]


# all users are able to view listed posts, but only logged in users can edit/delete

# need a 'read more' link to show full review for all users
# 'read more' then needs to take to a details view
# create detail view and link on list


