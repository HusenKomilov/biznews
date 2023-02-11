from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    text = models.TextField(verbose_name="Matn")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aloqa"
        verbose_name_plural = "Aloqalar"


class Mail(models.Model):
    mail = models.EmailField(unique=True, verbose_name="Email kiritadigan maydon")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Pochta'
        verbose_name_plural = 'Pochtalar addresi'