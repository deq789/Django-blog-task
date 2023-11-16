from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('apps.home:home_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        url = reverse('apps.home:home_view')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
