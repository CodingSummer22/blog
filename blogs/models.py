from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=140)
    date_created = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title + " (" + self.user.username + ")"
