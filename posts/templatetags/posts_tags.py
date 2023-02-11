from django import template
from posts.models import CategoryPosts, PostArticles, Comments
from django.db.models import Count, Max

register = template.Library()


@register.simple_tag()
def posts_tags():
    return CategoryPosts.objects.all()


@register.simple_tag()
def posts_articles():
    article = PostArticles.objects.filter(is_published=True).order_by(
        '-watched').select_related('category')
    return article[:5]


@register.simple_tag()
def posts_article_index():
    article = PostArticles.objects.filter(is_published=True).select_related(
        'category')
    return article.order_by('-watched')[:3]


@register.simple_tag()
def posts_article_slider():
    article = PostArticles.objects.filter(is_published=True).select_related(
        'category')
    return article[:4]


@register.simple_tag()
def count_comments(pk):
    ars = PostArticles.objects.get(pk=pk)
    comments = Comments.objects.filter(articles=ars).count()
    return comments

