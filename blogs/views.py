from django.shortcuts import render

from blogs.models import Blog


def blogs(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blogs.html', context)
