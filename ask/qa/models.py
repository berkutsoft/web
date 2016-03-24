from django.db import models
from django.contrib.auth.models import User

class Question (models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    raiting = models.IntegerField() 
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)

class Answer (models.Model):
    question = models.IntegerField()
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
   
