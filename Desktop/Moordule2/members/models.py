from django.db import models

# Create your models here.
class Members(models.Model):
    username = models.CharField(max_length=50)
    nikename = models.CharField(max_length=50)
    content = models.TextField(max_length=200, null=True)
