from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class CategoryPosts(models.Model):
    title = models.CharField(max_length=150, verbose_name="Maqola kategoriyasi", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_filter', kwargs={'category_name': self.title})

    class Meta:
        verbose_name = "Maqola kategoriyasi"
        verbose_name_plural = "Maqolalar kategoriyalari"


class PostArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name="Maqola sarlavhasi")
    content = models.TextField(verbose_name="Maqola matni")
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name="Maqola rasmi")
    watched = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name="Maqola yaratilgan vaqti")
    update_ad = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    is_published = models.BooleanField(default=True, verbose_name="Saytga qo'yishga ruxsat borligi")
    category = models.ForeignKey(CategoryPosts, on_delete=models.CASCADE, verbose_name="Maqola kategoriyasi")
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, verbose_name="Muxarrir")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('article_details', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"


class Comments(models.Model):
    articles = models.ForeignKey(PostArticles, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

# Create your models here.
