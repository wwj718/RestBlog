#coding:utf-8
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
	#api

    url(r'^list/',TemplateView.as_view(template_name="list.html"), name="blog_list"),
)