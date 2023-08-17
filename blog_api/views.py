from django.shortcuts import render
from rest_framework import generics
from blog.models import Post 
from .serializers import PostSerializer

class Father:
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostList(Father, generics.ListCreateAPIView):
    pass

class PostDetail(Father, generics.RetrieveDestroyAPIView):
    pass

class PostUpdate(Father, generics.UpdateAPIView):
    pass