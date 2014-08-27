#coding:utf-8
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='blog')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

#restful架构的关键 数据和表现分离
#动作
