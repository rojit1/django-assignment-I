from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    updated_at = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
