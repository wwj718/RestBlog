#coding:utf-8
from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User

#Hyperlinked - 超链接
# 类比 modelform?
#数据层面上只有两类，集合和detail
#双向?
#在抽象层面上，restful的许多动作是一致的，动作/数据，所以多数时候只要声明

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = Blog
        fields = ('url', 'owner','title', 'content', 'publish')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog = serializers.HyperlinkedRelatedField(view_name='blog-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'blog')
