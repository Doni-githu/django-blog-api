from django.urls import path
from .views import CategoryList


app_name = "category_api"

urlpatterns = [
    path("", CategoryList.as_view(), name="listcategory")
]
