from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=50)
    comment = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
