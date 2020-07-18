from django.shortcuts import render, HttpResponse, loader
from .models import Post
from datetime import datetime


def homepage(request):
    now = datetime.now()
    posts = Post.objects.all()
    template = loader.get_template('mainsite/index.html')
    html = template.render(locals())
    return HttpResponse(html)
