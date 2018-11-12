from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Question(models.Model):
    difficulties = [
        ('B',"Beginner"),
        ("E","Easy"),
        ("M","Medium"),
        ("H","Hard"),
    ]
    questionName = models.CharField(max_length=100)
    difficulty = models.CharField(choices = difficulties, max_length=50)
    questionLink = models.URLField(max_length=500)
    solutionLink = models.URLField(max_length=500)
    summary = models.TextField()
    addedBy = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.questionName
        

class Tag(models.Model):
    tagname = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tagname