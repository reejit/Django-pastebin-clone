from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    num_snippets = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class SnippetModel(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
