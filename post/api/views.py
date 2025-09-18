from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from ..models import Post
from .serializers import PostSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def post_view(request:Request):
    if request.method == "GET":
        posts = Post.objects.all()
        response = PostSerializer(posts,many=True)
        return Response(data=response.data,status=200)
        
    elif request.method == 'POST':
         data = request.data

         data = PostSerializer(data=data)

         if data.is_valid():
           print(data.validated_data)
           post = Post(**data.validated_data)
           post.save()
           return Response(data=data.data,status=201) 
         return Response(data=data.errors,status=400)


class TestView(APIView):

    def get(self,request):
        return Response(data={"method" : "GET"})
    
    def post(self,request):
        return Response(data={"method" : "post"})
    
    def put(self,request):
        return Response(data={"method" : "put"})
   
    def patch(self,request):
        return Response(data={"method" : "patch"})