from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here
class Post(models.Model):
    description=models.CharField(max_length=255)
    pic=models.ImageField(upload_to='path/to/img')
    date_posted=models.DateTimeField(default=timezone.now)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    tags=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('post-details',kwargs={'pk':self.pk})


class Comments(models.Model):
    post=models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    username=models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    comment=models.CharField(max_length=255)
    comment_date=models.DateTimeField(default=timezone.now)

class Likes(models.Model):
    user=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)



