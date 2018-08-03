from django.db import models


# Create your models here.
# Create your models here.
class Task(models.Model):
    # 爬虫名字
    name = models.CharField(max_length=200)
    # 爬虫备注
    memo = models.CharField(max_length=200)
    # 爬虫所在路径
    path = models.CharField(max_length=400)
    # 爬虫类型：0.普通爬虫 1.Scarpy
    type = models.IntegerField(default=0)
    # 创建时间
    createTime = models.DateTimeField(auto_now_add=True)
    # 最后修改时间
    lastModifyTime = models.DateTimeField(auto_now=True)
