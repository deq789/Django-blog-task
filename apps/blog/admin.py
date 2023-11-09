from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title',  'author', 'is_online', 'publication_datetime']


admin.site.register(Article, ArticleAdmin)
