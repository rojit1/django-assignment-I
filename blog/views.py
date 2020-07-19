from django.shortcuts import render
from .models import Blog


def home_view(request):
    return render(request, 'blog/home.html')


def blog_view(request):
    blogs = Blog.objects.all()
    print(len(blogs))
    return render(request, 'blog/blog.html', {'blogs': blogs})
