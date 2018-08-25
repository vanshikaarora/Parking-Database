from datetime import timezone

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, DatePost
from .forms import PostForm, DateForm
from django.db import models
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

@csrf_exempt
def post_detail(request, number,id=None):
    post = get_object_or_404(Post,number=number)
    return render(request, 'park/post_detail.html', {'post': post})

@csrf_exempt
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'park/post_list.html', {'posts': posts})

#@csrf_protect
#@ensure_csrf_cookie
@csrf_exempt
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', number=post.number)
    else:
        form = PostForm()
    return render(request, 'park/post_edit.html', {'form': form})


def post_dates(request,number):
    #posts = DatePost.objects.all()
    posts=DatePost.objects.get(id=id)
    #posts = get_object_or_404(Post,pk=pk)
    #posts=get_object_or_404(Post,number=number)
    return render(request,'park/post_dates.html',{'posts':posts})


def post_update(request):
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',id=post.id)
    else:
        form = DateForm()
    return render(request, 'park/post_update.html', {'form': form})