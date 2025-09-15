from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
# Create your views here.


def post_view(request):

    # try:
        
    # except:
    posts = Post.objects.all()

       
    return render(request, 'all_posts.html',{
        "posts" : posts
    })

def create_post_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file')
        post = Post(title=title, content=content, file=file)
        print(post)
        post.save()
        return redirect('post')
    else:
          return render(request, 'post.html')
    
def detail_view(request,id):
     try:

        post = Post.objects.get(id=id)
     except : 
         return HttpResponse("Post Not Found")
     
     if request.method == "POST":
        print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file')
        post.title = title
        post.content = content
        if file:
            post.file = file

        post.save()
        return redirect('post')
     

     return render(request,'post_detail.html',{
          "post" : post
     })

def delete_view(request,id):
     


   
    try:

        post = Post.objects.get(id=id)
        post.delete()

        return redirect('post')
    except : 
         return HttpResponse("Post Not Found")

    