#coding:utf-8
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from blog.models import Blog
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import BlogSerializer, UserSerializer

#包装了太多层了...设计是为了重用
#初学还是从底层开始吧，易于定制
#否则到处牵扯

#起什么作业，做了些什么, 类比
class BlogViewSet(viewsets.ModelViewSet):
    """
    BlogViewSet
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # @link(renderer_classes=(renderers.StaticHTMLRenderer,))
    # def highlight(self, request, *args, **kwargs):
    #     bolg = self.get_object()
    #     return Response(bolg.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    UserViewSet
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
