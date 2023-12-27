from django.db import models
from post.models import Post

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments'
    )





        
# написать модельку коментариев в отдельном приложении соment 
# с полями content, owner, created_at, post, 
# crud & serializer & @action 