from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='',blank=False)
    file = models.FileField()
    marks = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    submission_date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    question = models.CharField(max_length=255)
    marks = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    assignment = models.ForeignKey(Assignment)
    
    def __str__(self):
        return self.question

class Answers(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField(default='')
    correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer
    
    