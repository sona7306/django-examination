from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_Blogger = models.BooleanField(default=False)


class Blogger(models.Model):
    blogger_detail = models.OneToOneField("Login", on_delete=models.CASCADE)
    name = models.CharField()
    email = models.EmailField()
    bio = models.TextField()
    document = models.FileField(upload_to='documents/')



class BlogPost(models.Model):
    blog_detail = models.ForeignKey("blogger", on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField()
    document = models.FileField(upload_to='documents/')
    date = models.DateField()