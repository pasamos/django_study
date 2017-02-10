from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    loginCount = models.IntegerField(default=0)
    
    def __str__(self):
        return 'name:'+self.name + '-age:' + str(self.age) + '-sex:' + self.sex+ '-login count:' + str(self.loginCount)
