from django.shortcuts import render, HttpResponse
from .models import Post
from datetime import datetime


def homepage(request):
    now = datetime.now()
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append('No.{}'.format(str(count)) + str(post.title) + '<br>')
        post_lists.append('<small>' + str(post.body)
                          + '</small><br><br>')
    print(post_lists)
    return HttpResponse(post_lists)
