from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View
from decouple import config

from .forms import ContactForm


class ContactView(View):
    template_name = 'contact_form.html'
    success_template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Send an email
            subject = 'Django blog task'
            message = f'Name: {form.cleaned_data["name"]}\nContent: {form.cleaned_data["content"]}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [config('RECIPIENT')]

            msg = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list,
                reply_to=[form.cleaned_data["email"]],
            )

            msg.send()
            return render(request, self.success_template_name)  # Render success template

        return render(request, self.template_name, {'form': form})
