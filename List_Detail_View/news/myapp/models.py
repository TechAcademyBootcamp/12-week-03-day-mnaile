from django.db import models

# Create your models here.

class News(models.Model):
    image = models.ImageField(upload_to='news/image/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    author = models.CharField(max_length=255)
