from rest_framework import serializers
from blog.models import Blog
from django.contrib.auth.models import User


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
