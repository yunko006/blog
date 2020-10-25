from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):

    """Une class qui contient le model d'un blog post"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

