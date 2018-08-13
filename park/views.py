from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'park/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'park/post_list.html', {'posts': posts})

@csrf_exempt
def post_new(request):
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
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    return render(request, 'park/post_edit.html', {'form': form})