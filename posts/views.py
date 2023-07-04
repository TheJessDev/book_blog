from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DetailView,
)
from .models import Post
from django.urls import path
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect



class LoginView(LoginView):
    template_name = 'posts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('home')

        return self.form_invalid(form)




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
    
    



