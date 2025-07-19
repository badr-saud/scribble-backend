from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7, default="#ffffff")

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_notes")

    def __str__(self):
        return self.title
