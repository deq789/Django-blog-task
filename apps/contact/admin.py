from django.contrib import admin

from .models import ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'date']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ContactRequest, ContactRequestAdmin)

