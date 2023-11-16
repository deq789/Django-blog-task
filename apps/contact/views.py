from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic.edit import FormView

from decouple import config

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/success/'

    def form_valid(self, form):
        # Send a confirmation email with contact form data
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

        return super().form_valid(form)
