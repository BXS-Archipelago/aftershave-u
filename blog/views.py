from django.db.models import Q
from django.shortcuts import  get_object_or_404, render
from .models import Post, Brands

def detail(request, brands_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    return render(request, 'blog/detail.html', {'post': post})


def brands(request, slug):
    brands = get_object_or_404(Brands, slug=slug)
    posts = brands.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/brands.html', {'brands': brands, 'posts':posts })


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(
        intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})
