from __future__ import unicode_literals

from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
