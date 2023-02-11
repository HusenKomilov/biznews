from django import forms
from .models import PostArticles, Comments
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostArticlesForms(forms.ModelForm):
    class Meta:
        model = PostArticles
        fields = ('title', 'content', 'photo', 'is_published', 'category', 'author')

        widgets = {
            'title': forms.TextInput(attrs={
                "placeholder": "Sarlavha matni",
                "class": "form-control"
            }),
            'content': forms.Textarea(attrs={
                "placeholder": "Maqola matni",
                "class": "form-control"
            }),
            'is_published': forms.CheckboxInput(attrs={
                "placeholder": "Saytga qo'yishga ruxsat",
                "class": "form-check"
            }),
            'category': forms.Select(attrs={
                "placeholder": "Maqola kategoriyasi",
                "class": "form-select form-select-lg mb-3"
            }),
            'author': forms.Select(attrs={
                "placeholder": "Maqola muharriri",
                "class": "form-select"
            })
        }


class CommentForms(forms.ModelForm):
    class Meta:

        model = Comments
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={
                "placeholder": "Komentariya qo'shish",
                "class": "form-control",
            })
        }
