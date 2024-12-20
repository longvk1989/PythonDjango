from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

def hello_world(request):
    return HttpResponse('Hello World HTTPResponse')

def hello_html(request):
    return render(request, 'myapp/hello.html')

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'myapp/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content)
        post.save()
        return redirect('post_list')
    return render(request, 'myapp/create_post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'myapp/post_detail.html', {'post': post})

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/delete_post.html', {'post': post})
