from django.shortcuts import render
from django.template import Context
from models import BlogPost


def archive(request):
    """
    fetch all blog post data from database,
    render them with template, and return rendered string.
    """

    return render(request, 'archive.html',
                  context=Context({'posts': BlogPost.objects.all()}))
