from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    # published posts
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects
        context["object_list"] = context["post_list"]
        return context




