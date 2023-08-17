from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class BlogListView(TemplateView):
    template_name = "blog/index.html"
