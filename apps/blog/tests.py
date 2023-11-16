from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.blog.models import Article


class ArticleModelTest(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title="Test Article", content="Content for the test article.",
                                              author=self.author)

    def test_article_creation(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.content, "Content for the test article.")


class ArticleViewsTest(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='testuser', password='testpassword')
        self.article = Article.objects.create(title="Test Article", content="Content for the test article.",
                                              author=self.author)

    def test_article_list_view(self):
        response = self.client.get(reverse('apps.blog:articles'))
        self.assertEqual(response.status_code, 200)

    def test_article_detail_view(self):
        response = self.client.get(reverse('apps.blog:article_detail', args=[self.article.slug, self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")
