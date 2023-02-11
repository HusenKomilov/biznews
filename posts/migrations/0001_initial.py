# Generated by Django 4.1.6 on 2023-02-08 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Maqola kategoriyasi')),
            ],
            options={
                'verbose_name': 'Maqola kategoriyasi',
                'verbose_name_plural': 'Maqolalar kategoriyalari',
            },
        ),
        migrations.CreateModel(
            name='PostArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Maqola sarlavhasi')),
                ('content', models.TextField(verbose_name='Maqola matni')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/', verbose_name='Maqola rasmi')),
                ('watched', models.IntegerField(default=0, verbose_name="Ko'rishlar soni")),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='Maqola yaratilgan vaqti')),
                ('update_ad', models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')),
                ('is_published', models.BooleanField(default=True, verbose_name="Saytga qo'yishga ruxsat borligi")),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Muxarrir')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.categoryposts', verbose_name='Maqola kategoriyasi')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postarticles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]