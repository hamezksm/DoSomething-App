from django.db import models

# Create your models here.

class boards(models.Model):
    board_name=models.CharField(max_length=25,unique=True)
    description=models.TextField(max_length=150)
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(unique=True,max_length=15)
    time_uploaded=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    post=models.TextField(max_length=250)

    def __str__(self):
        return self.post
    