from django.views.generic import ListView, CreateView
from .models import Post
from django.urls import path

class PostListView(ListView):
    # published posts
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects
        context["object_list"] = context["post_list"]
        return context

class PostCreateView(CreateView):
    template_name = "posts/create_post.html"
    model = Post
    fields = ["book_title", "book_author", "post_author", "body"]
    



