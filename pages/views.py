from django.shortcuts import render
from posts.models import PostArticles, Comments
from django.views.generic import ListView, DetailView
from django.db.models import Q
import datetime as dt


# Create your views here.

# Home pages
class Index(ListView):
    model = PostArticles
    context_object_name = 'articles'
    template_name = 'pages/index.html'
    date = dt.datetime.now()
    x = date.strftime("%d-%B-%Y Soat: %H:%M")
    extra_context = {
        "title": "Haqiqat achchiq bo'ladi",
        'date': x
    }

    def get_queryset(self):
        articles = PostArticles.objects.filter(is_published=True).select_related('category')
        return articles


# Category page
def category(request):
    articles = PostArticles.objects.filter(is_published=True).order_by('-pk').select_related('category')
    date = dt.datetime.now()
    x = date.strftime("%d-%B-%Y Soat: %H:%M")
    context = {
        "title": "Categoriyalar",
        'articles': articles,
        'date': x
    }
    return render(request, 'pages/category.html', context)


# Category pages all articles
class CategoryListAll(ListView):
    model = PostArticles
    context_object_name = 'articles'
    template_name = "pages/category.html"
    extra_context = {"title": "Barcha maqolalar"}

    def get_queryset(self):
        articles = PostArticles.objects.filter(is_published=True).order_by('-pk').select_related('category')
        return articles


def category_filter(request, category_name):
    article = PostArticles.objects.filter(category__title=category_name).order_by('-pk').select_related('category')
    context = {
        "articles": article,
        "category_name": category_name
    }
    return render(request, 'pages/category_filter.html', context)


class SearchPostArticle(Index):
    template_name = 'pages/category.html'

    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = PostArticles.objects.filter((Q(title__icontains=word) | Q(content__icontains=word)),
                                            is_published=True).select_related('category')
        return articles

def error_404(request, exception):
    return render(request, '404.html')
