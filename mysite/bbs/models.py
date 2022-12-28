from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    slag = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField(max_length=1000)

    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
