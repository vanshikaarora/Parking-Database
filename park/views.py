from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.db import models
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator

@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'park/post_detail.html', {'post': post})

@csrf_exempt
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'park/post_list.html', {'posts': posts})

#@csrf_protect
#@ensure_csrf_cookie
@csrf_exempt
def post_new(request):
    print(request.method)#+" "+request.method+" "+request.data+" "+ request.url)
    print(request.body)
    if request.method == "POST":
        print (request.body)
        fake = request.body
        fakedata = str(fake)
        print(fakedata)
        fakedatas = fakedata.split('&')
        VT = fakedatas[0].split("=")[1]
        VN = fakedatas[1].split("=")[1]
        VA = fakedatas[2].split("=")[1]
        VTi = fakedatas[3].split("=")[1].split("'")[0]
        #VT=fakedatas[3]
        #VN=fakedatas[7]
        #VA=fakedatas[11]
        #VTi=fakedatas[15]
        #print(fakedata.split('"')[3])
        #print(VN+" "+VA+" "+VTi)
        #formsear = Post.objects.create(vehicleType = VT, number = VN, amount = VA, timeIn = VTi)
        #print (formsear)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.number)
        else:
            form = PostForm()
    if request.method == "PUT":
        fake = request.body
        print(fake)
        fakedata = str(fake)
        fakedatas = fakedata.split('&')
        VT = fakedatas[0].split("=")[1]
        VN = fakedatas[1].split("=")[1]
        VA = fakedatas[2].split("=")[1]
        VTi=fakedatas[3].split("=")[1]
        VTo = fakedatas[4].split("=")[1].split("'")[0]
        #VT=fakedatas[3]
        #VN=fakedatas[7]
        #VA=fakedatas[11]
        #VTi=fakedatas[15]
        #print(fakedata.split('"')[3])
        print(VN+" "+VA+" "+VTi)
        #form = Post.objects.create(vehicleType = VT, number = VN, amount = VA, timeIn = VTi, timeOut = VTo)
        form=Post.add_to_class('timeOut',VTo)
        print (VTo)
        print((form))
    return render(request, 'park/post_edit.html', {'form': form})