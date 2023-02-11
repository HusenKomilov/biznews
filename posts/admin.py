from django.contrib import admin
from .models import CategoryPosts, PostArticles, Comments


# Register your models here.
@admin.register(PostArticles)
class PostArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_ad', 'update_ad', 'is_published', 'category', 'author',)
    list_editable = ('is_published', 'category', 'author',)
    list_display_links = ('pk', 'title')
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(CategoryPosts)
admin.site.register(Comments)