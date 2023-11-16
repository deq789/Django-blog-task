from django.core.mail import EmailMessage
from django.conf import settings

from decouple import config


def send_email(subject, form):
    """Sends an email with received form data."""

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
