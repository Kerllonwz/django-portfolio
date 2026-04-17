from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/detail.html', {'post': post, 'posts': posts})
