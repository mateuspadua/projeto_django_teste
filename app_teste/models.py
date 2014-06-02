from django.db import models

# Create your models here.

class Blog(models.Model):
    post = models.TextField("post", blank=True, null=True)
    date = models.DateTimeField("Data postagem", blank=True, null=True, default=None)
    
