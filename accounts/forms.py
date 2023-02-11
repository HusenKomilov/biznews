from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Contact, Mail


class Login(AuthenticationForm):
    username = forms.CharField(label="Foydalanuvchi ismi",
                            widget=forms.TextInput(attrs={
                                "placeholder": "Ismingizni kiriting",
                                "class": "form-control"
                            }))
    password = forms.CharField(label="Parol",
                            widget=forms.PasswordInput(attrs={
                                "placeholder": "Parolni kiriting",
                                "class": "form-control"
                            }))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=100, help_text="Ko'pi bilan 100ta simvol kiritshingiz mumkin",
                            widget=forms.TextInput(attrs={
                                'placeholder': "Ismingizni kiriting",
                                "class": "form-control",
                                "style": "margin:20px"
                            }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Parol kiriting",
        "style": "margin:20px"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "Parolni tasdiqlang",
        "style": "margin:20px"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': "emaillingizni kiriting",
        "style": "margin:20px"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'text')

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ismingizni kiritng",
                "class": 'form-control'
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Emailingizmi kiritng",
                "class": "form-control"
            }),
            'subject': forms.TextInput(attrs={
                "placeholder": "Subject",
                "class": "form-control"
            }),
            'text': forms.Textarea(attrs={
                "placeholder": "Xabaringizni yuboring",
                "class": "form-control"
            })
        }


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('mail',)

        widgets = {
            'mail': forms.EmailInput(attrs={
                'placeholder': "Emailni registratsiya qilish",
                'class': "form-control form-control-lg"
            })
        }
