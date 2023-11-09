from django.db import models
from django.utils import timezone


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.email}"
