from django.urls import path
from .views import *


app_name = "category_api"

urlpatterns = [
    path("", CategoryList.as_view(), name="listcategory"),
    path("<int:pk>/", CategoryDetail.as_view(), name="detaildelete"),
    path("edit/<int:pk>/", CategoryUpdate.as_view(), name="update")
]
