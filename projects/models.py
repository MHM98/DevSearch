from operator import mod, truediv
from django.db import models
from django.db.models.base import Model
import uuid
from users.models import profile

from django.db.models.deletion import CASCADE, SET_NULL
# Create your models here.

class project(models.Model):
    owner=models.ForeignKey(profile , null=True , blank=True , on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    featured_image=models.ImageField(null=True,blank=True ,default="default.jpg")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    tags=models.ManyToManyField('Tag',blank=True)
    total_vote=models.IntegerField(default=0,null=True,blank=True)
    total_ratio=models.IntegerField(default=0,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering=['-total_ratio','-total_vote','title']


    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
        
    @property 
    def getVoteCount(self):
        # get all reviews
        reviews=self.review_set.all()
        upVotes=reviews.filter(value='up').count()
        totalVOtes=reviews.count()
        ratio=(upVotes/totalVOtes)* 100

        self.total_ratio=ratio
        self.total_vote=totalVOtes

        self.save()


class Review(models.Model):
    VOTE_TYPE=(
        ('up','up vote'),
        ('down','down vore')
    )
    owner=models.ForeignKey(profile,on_delete=models.CASCADE , null=True)
    project=models.ForeignKey(project,on_delete=CASCADE) #when project has delete,the reveiw fild will be delete too   
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)

    class Meta:
        unique_together=[['owner','project']]
        
    def __str__(self):
        return self.value

class Tag(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    def __str__(self):
        return self.name