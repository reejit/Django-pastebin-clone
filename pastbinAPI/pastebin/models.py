from django.db import models


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
