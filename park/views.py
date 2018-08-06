from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'park/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'park/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'park/post_edit.html', {'form': form})