from django.shortcuts import render
from .models import Post

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/detail.html', {'post': post})
