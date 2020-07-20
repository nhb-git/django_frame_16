from django.shortcuts import render, HttpResponse, loader, redirect
from .models import Post
from datetime import datetime
from .forms import ContactForm


def homepage(request):
    now = datetime.now()
    posts = Post.objects.all()
    template = loader.get_template('mainsite/index.html')
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = loader.get_template('mainsite/post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


def register(request):
    form = ContactForm()
    if request.method == 'GET':
        return render(request, 'mainsite/register.html', locals())
