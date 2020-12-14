from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogImage

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_key):
    detailblog = get_object_or_404(Blog, blog_key=blog_key)
    images = BlogImage.objects.filter(blog=detailblog)
    return render(request, 'blog/detail.html', {
        'blog':detailblog,
        'images':images   
        })
