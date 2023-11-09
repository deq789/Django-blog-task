from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_datetime = models.DateTimeField(default=timezone.now)
    is_online = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generate slug from title
        self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        """
        Generate a unique slug based on the article title.
        """
        slug = self.title.lower().replace(' ', '-')
        unique_slug = slug
        num = 2
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    def __str__(self):
        return f"{self.title} - {self.slug}"


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.email}"
