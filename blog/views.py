from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  return render(request, "index.html", {"posts": posts})
