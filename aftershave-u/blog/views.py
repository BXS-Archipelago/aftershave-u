from django.shortcuts import  get_object_or_404, render
from .models import Post, Brands, Creators

def detail(request, brands_slug, creators_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/detail.html', {'post': post})


def brands(request, slug):
    brands = get_object_or_404(Brands, slug=slug)
    posts = brands.posts.all()

    return render(request, 'blog/brands.html', {'brands': brands, 'posts': posts})


def creators(request, slug):
    creators = get_object_or_404(Creators, slug=slug)
    posts = creators.posts.all()

    return render(request, 'blog/creators.html', {'creators': creators, 'posts': posts})