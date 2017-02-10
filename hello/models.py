from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + '-' + str(self.age) + '-' + self.sex
