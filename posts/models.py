from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title