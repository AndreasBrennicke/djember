from django.db import models

class Book(models.Model):
    title       = models.CharField(max_length=512)
    author      = models.CharField(max_length=100)
    description = models.TextField()
    date        = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']