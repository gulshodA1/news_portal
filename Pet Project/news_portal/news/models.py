from django.contrib.auth.models import User
from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    section=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/')
    views=models.IntegerField(default=0)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.article.title}"
        
