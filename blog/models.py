from django.db import models

class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    publish = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='blog')

    class Meta:
        ordering = ('created',)
