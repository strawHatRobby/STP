from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField(default='invalid description',blank=False)
    Credits = models.IntegerField(default=0)
    started_on = models.DateField(null=True,blank=False)
    ends_on = models.DateField(null=True,blank=False)
    
    def __str__(self):
        return self.course_name
    

    