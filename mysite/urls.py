#coding:utf-8
from blog import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'blog', views.BlogViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)), #need format so don't use it  just use to debug
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^blog/', include("blog.urls")),
)


#http://git.oschina.net/wuwenjie/murp_edx/wikis/django-rest-framework--%E7%AC%94%E8%AE%B0
#http://git.oschina.net/wuwenjie/murp_edx/wikis/django-rest