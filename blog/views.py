from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post-detail.html", {"post": post})