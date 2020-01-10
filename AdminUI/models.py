from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200,null=False)
    url = models.CharField(max_length=500,unique=True,null=False)
    category = models.CharField(max_length=200,default='Default Category')
    featuring = models.CharField(max_length=100,null=False)
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title