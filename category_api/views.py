from django.shortcuts import render
from rest_framework import generics
from blog.models import Category
from .serializers import CategorySerializer

class CategoryFather:
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(CategoryFather,generics.ListCreateAPIView):
    pass

class CategoryDetail(CategoryFather, generics.RetrieveDestroyAPIView):
    pass

class CategoryUpdate(CategoryFather, generics.UpdateAPIView):
    pass
