from django.db import models

# Create your models here.
class add(models.Model):
    title=models.CharField(max_length=200,unique=True)
    des=models.TextField()

