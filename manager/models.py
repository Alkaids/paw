from django.db import models


class Project(models.Model):
    # spider name
    name = models.CharField(max_length=200)
    # spider memo
    memo = models.CharField(max_length=200)
    # spider path
    path = models.CharField(max_length=400)
    # spider type
    type = models.IntegerField(default=0)
    # createTime
    createTime = models.DateTimeField(auto_now_add=True)
    # lastModifyTime
    lastModifyTime = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    # setting name
    name = models.CharField(max_length=200)
    # setting value
    value = models.CharField(max_length=200)
