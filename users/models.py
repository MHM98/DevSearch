
import builtins
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
# Create your models here.



class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE , null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    location=models.CharField(max_length=200,blank=True,null=True)
    short_intro=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length=200,blank=True,null=True)
    social_twitter=models.CharField(max_length=200,blank=True,null=True)
    social_linkedin=models.CharField(max_length=200,blank=True,null=True)
    social_youtube=models.CharField(max_length=200,blank=True,null=True)
    social_website=models.CharField(max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return str(self.user.username)
    
    


class Skill(models.Model):
    owner=models.ForeignKey(profile,on_delete=CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    sender=models.ForeignKey(profile,on_delete=models.SET_NULL,blank=True,null=True)
    recipient=models.ForeignKey(profile,on_delete=models.SET_NULL,blank=True,null=True,related_name="messages")
    name=models.CharField(max_length=200,blank=True,null=True)
    is_read=models.BooleanField(default=False)
    subject=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200,null=True,blank=True)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering=['is_read','-created']