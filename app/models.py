from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(unique=True,max_length=15)
    time_uploaded=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    post=models.TextField(max_length=250)

    def __str__(self):
        return self.post
    