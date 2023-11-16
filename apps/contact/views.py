from django.views.generic.edit import FormView

from .forms import ContactForm
from .utils import send_email


class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()

        # Send a confirmation email with contact form data
        send_email("Django blog task", form)

        return super().form_valid(form)
