from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

@login_required()
def post_view(request):

    # try:
        
    # except:
    posts = Post.objects.all()

       
    return render(request, 'all_posts.html',{
        "posts" : posts
    })

def create_post_view(request):
    if request.method == "POST":
        postForm = PostForm(request.POST,request.FILES)
        if postForm.is_valid():
            postForm.save()
        
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # file = request.FILES.get('file')
        # post = Post(title=title, content=content, file=file)
        # print(post)
        # post.save()
        return redirect('post')
    else:
        postForm = PostForm()
        return render(request, 'post.html',{'form' : postForm})
    
def detail_view(request,id):
     try:

        post = Post.objects.get(id=id)
     except : 
         return HttpResponse("Post Not Found")
     
     if request.method == "POST":
        # print(request.POST)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # file = request.FILES.get('file')
        # post.title = title
        # post.content = content
        # if file:
        #     post.file = file

        # post.save()
        postForm = PostForm(request.POST,request.FILES,instance=post)
        if postForm.is_valid():
            postForm.save()
        return redirect('post')
     
     form = PostForm(instance=post)
     return render(request,'post_detail.html',{
          "post" : post,
          "form" : form
     })

def delete_view(request,id):
     


   
    try:

        post = Post.objects.get(id=id)
        post.delete()

        return redirect('post')
    except : 
         return HttpResponse("Post Not Found")

    