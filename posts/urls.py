from django.urls import path
from .views import *

urlpatterns = [
    path('new/', create_post_articles, name="new"),
    path('details/<int:pk>/', PostsArticlesDetails.as_view(), name="article_details"),
    path('delete/<int:pk>/', PostArticlesDelete.as_view(), name="delete"),
    path('update/<int:pk>/', PostArticleUpdateView.as_view(), name="update"),
    path('add_comment/<int:articles_id>/', add_comment, name="add_comment"),
    path('comments/<int:article_id>/', post_article_comments, name="comments"),
]