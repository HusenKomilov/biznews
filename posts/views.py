from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import PostArticles, CategoryPosts, Comments
from .forms import PostArticlesForms, CommentForms
from django.views.generic import DeleteView, UpdateView, DetailView
from django.contrib import messages


# Create your views here.

def create_post_articles(request):
    if request.method == "POST":
        form = PostArticlesForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostArticlesForms
        context = {
            "title": "Maqola qo'shish",
            'form': form
        }
        return render(request, 'posts/new_article.html', context)


class PostsArticlesDetails(DetailView):
    model = PostArticles
    context_object_name = 'posts'
    template_name = 'posts/detail.html'
    extra_context = {"title": "Batafsil qismi"}

    def get_queryset(self):
        return PostArticles.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = PostArticles.objects.get(pk=self.kwargs['pk'])
        article.watched += 1
        article.save()

        context['title'] = article.title
        comment = Comments.objects.filter(articles=article)
        count = comment.count()
        context['count'] = count
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForms()

        return context


class PostArticlesDelete(DeleteView):
    model = PostArticles
    extra_context = {"title": "Maqolani o'chirish"}
    success_url = reverse_lazy('index')


class PostArticleUpdateView(UpdateView):
    model = PostArticles
    form_class = PostArticlesForms
    extra_context = {"title": "Maqolani o'zgartirish"}
    template_name = 'posts/new_article.html'


def add_comment(request, articles_id):
    form = CommentForms(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        article = PostArticles.objects.get(pk=articles_id)
        comment.articles = article
        comment.save()
        messages.success(request, "Komentatiyangiz saqlandi")
        return redirect('article_details', articles_id)


def post_article_comments(request, article_id):
    article = PostArticles.objects.get(pk=article_id)
    comment = Comments.objects.filter(articles=article)
    count = comment.count()

    context = {
        'comments': comment,
        'articles': article
    }
    return render(request, 'posts/comments.html', context)
