from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import Login, RegistrationForm, ContactForm, MailForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from posts.models import PostArticles
from .models import Mail


# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = Login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Siz saytga tashrif buyurdingiz")
            return redirect('index')
    else:
        form = Login()
    context = {
        "title": "Saytga kirish",
        "form": form
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "Siz saytdan chiqib kettingiz")
    return redirect('login')


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akkauntga kirishingiz mumkin")
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        "title": "Ro'yxatdan o'tish",
        "form": form
    }
    return render(request, 'accounts/registration.html', context)


@login_required()
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    articles = PostArticles.objects.filter(author=user)
    context = {
        "title": "Sizning profileningiz",
        "users": user,
        "articles": articles.order_by('-pk')
    }
    return render(request, 'accounts/profile.html', context)


def contacts(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sizning xabaringiz yuborildi.")

    else:
        form = ContactForm()
    context = {
        "title": "Aloqa uchun",
        "form": form
    }
    return render(request, 'accounts/contact.html', context)


