from django.db import models
# import django User
from django.contrib.auth.models import User


# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, default=None)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Video(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True, default=None)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Email(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                related_name='sent_by')
