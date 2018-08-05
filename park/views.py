from django.shortcuts import render

def post_list(request):
    return render(request, 'park/post_list.html', {})
