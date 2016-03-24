from django.db import models
from django.contrib.auth.models import User

class Question (models.Model):
    class Meta:
        db_table = 'question'
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    raiting = models.IntegerField() 
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')

class Answer (models.Model):
    class Meta:
        db_table = 'question'
    question = models.IntegerField()
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
   
