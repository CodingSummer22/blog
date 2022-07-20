from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=140)
    date_created = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title + " (" + self.user.username + ")"


class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField(null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.RESTRICT)
    date_added = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(default=datetime.now)
    impressions = models.IntegerField(default=0)
    draft = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.title

