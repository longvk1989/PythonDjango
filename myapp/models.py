from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=280)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
