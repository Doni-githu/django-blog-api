from django.urls import path, include
from .views import *
from rest_framework import routers


app_name = "blog_api"

urlpatterns = [
    path("", PostList.as_view(), name="listcreate"),
    path("<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("edit/<int:pk>/", PostUpdate.as_view(), name="updatepost")
]
