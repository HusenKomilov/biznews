from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('all_posts/', CategoryListAll.as_view(), name='category'),
    path('search/', SearchPostArticle.as_view(), name="search_results"),
    path('category/<str:category_name>/', category_filter, name="category_filter"),
]
