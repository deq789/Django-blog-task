from django.contrib import admin

from .models import Article, ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'date']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title',  'author', 'is_online', 'publication_datetime']


admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(Article, ArticleAdmin)
