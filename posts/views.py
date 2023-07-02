from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DetailView,
)
from .models import Post
from django.urls import path
from django.contrib.auth.mixins import UserPassesTestMixin




class PostListView(ListView):
    # published posts
    template_name = "posts/lists.html"
    model = Post

    # def test_func(self):
    #     post = self.get_object()
    #     return post.author == self.request.user

class MyPostListView(ListView):
    template_name = "posts/my_lists.html"
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(post_author=self.request.user)
        return queryset

class PostCreateView(CreateView):
    template_name = "posts/create_post.html"
    model = Post
    fields = ["book_title", "book_author", "post_author", "body"]

class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post


class PostUpdateView(UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["book_title", "book_author", "post_author", "body"]

    def test_func(self):
        post = self.get_object()
        return post.post_author == self.request.user
    
    



