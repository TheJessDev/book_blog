from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
    DetailView,
)
from .models import Post, UserProfile
from django.urls import path, reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from .forms import UserProfileForm
from django.db.models import Q




# class LoginView(LoginView):
#     template_name = 'posts/login.html'

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
        

#         if user is not None:
#             login(self.request, user)
#             # authors = User.objects.exclude(id=user.id)
#             return redirect('list')

#         return self.form_invalid(form)

# class SignupView(CreateView):
#     template_name = "registration/signup.html"
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.save()
#         username=form.cleaned_data.get("username")
#         password=form.cleaned_data.get("password1")
#         user=authenticate(username=username, password=password)
#         return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfileForm
    form_class = UserProfileForm
    template_name = 'registration/profile_update.html'
    success_url = '/profile'

    def get_object(self, queryset=None):
        return self.request.user.userprofile


class PostListView(ListView):
    # published posts
    template_name = "posts/lists.html"
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class MyPostListView(ListView):
    template_name = "posts/my_lists.html"
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(post_author=self.request.user)
        return queryset

class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = "posts/create_post.html"
    model = Post
    fields = ["book_title", "book_author", "body"]

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post
    fields = ["book_title", "book_author", "post_author", "body"]
    


class PostUpdateView(UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["book_title", "book_author", "post_author", "body"]

    def test_func(self):
        post = self.get_object()
        return post.post_author == self.request.user
    
    
class PostSearchView(ListView):
    model = Post
    template_name = 'posts/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(book_title__icontains=query) |
                Q(body__icontains=query) 
                
            )
        else:
            return []
        



