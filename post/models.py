from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey(
        'auth.User', 
        related_name='posts',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
