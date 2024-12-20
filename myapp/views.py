from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def hello_world(request):
    return HttpResponse('Hello World HTTPResponse')

def hello_html(request):
    return render(request, 'myapp/hello.html')

@login_required
def post_list(request):
    posts = Post.objects.filter(user=request.user).order_by('-id')
    return render(request, 'myapp/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content, user=request.user)
        post.save()
        return redirect('post_list')
    return render(request, 'myapp/create_post.html')

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post_list')
    return render(request, 'myapp/post_detail.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'myapp/delete_post.html', {'post': post})

# signup - login - logout
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username da ton tai')
            return redirect('signup')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'Mat khau khong khop')
            return redirect('signup')

    return render(request, 'myapp/signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        else:
            messages.error(request, 'Username hay password khong dung')
            return redirect('login')

    return render(request, 'myapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
