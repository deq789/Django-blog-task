from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm


class ContactView(View):
    template_name = 'contact_form.html'
    success_template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})
