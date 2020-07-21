from django.shortcuts import render, HttpResponse, loader, redirect
from .models import Post
from datetime import datetime
from .forms import ContactForm
from .forms import PostForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('post')
    if request.method == 'GET':
        form = ContactForm()
    return render(request, 'mainsite/register.html', locals())


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponse('post')
    if request.method == 'GET':
        form = PostForm()
    return render(request, 'mainsite/post.html', locals())
