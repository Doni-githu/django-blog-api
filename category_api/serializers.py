from rest_framework import serializers
from blog.models import Category
from blog_api.serializers import PostSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'