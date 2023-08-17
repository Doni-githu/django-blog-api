from django.urls import path, include
from django.views.generic import TemplateView
from .views import *
app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="main")
]
