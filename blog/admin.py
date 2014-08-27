#coding:utf-8
from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    search_fields = ('title','content')
    fields = ('title','content')
    list_display = ('title','content')

admin.site.register(Blog, BlogAdmin)