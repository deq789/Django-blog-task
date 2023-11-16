from django.test import TestCase, Client
from django.urls import reverse

from apps.contact.models import ContactRequest


class ContactFormTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_form_submission(self):

        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'content': 'Test message content.'
        }

        # Simulate form submission
        response = self.client.post(reverse('apps.contact:contact_view'), form_data, follow=True)

        # Check that the form submission was successful
        self.assertEqual(response.status_code, 200)

        # Check that a new entry was created in the database
        self.assertEqual(ContactRequest.objects.count(), 1)
        new_entry = ContactRequest.objects.first()
        self.assertEqual(new_entry.name, 'John Doe')
        self.assertEqual(new_entry.email, 'john@example.com')
        self.assertEqual(new_entry.content, 'Test message content.')

    def test_contact_form_invalid_submission(self):
        # Simulate form submission with invalid data
        response = self.client.post('/contact/', {}, follow=True)

        # Check that no entry was created in the database
        self.assertEqual(ContactRequest.objects.count(), 0)
