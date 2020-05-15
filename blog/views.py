from django.shortcuts import render, get_object_or_404
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.order_by('-date_published')
    return render(request, "blogs/all_blogs.html", {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, "blogs/blog_details.html", {'blog': blog})
