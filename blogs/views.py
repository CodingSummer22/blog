from django.shortcuts import render

from blogs.models import Blog


def blogs(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blogs.html', context)


def blog(request, bid):
    context = {}
    context['blog'] = Blog.objects.get(id=bid)
    return render(request, 'blog.html', context)
