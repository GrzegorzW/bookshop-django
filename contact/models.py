from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=200)
    jingle = models.CharField(max_length=200)
    about = models.TextField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    logo = models.ImageField()
    smallLogo = models.ImageField()
    map = models.ImageField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.street + ' ' + self.city + ' ' + self.post_code


class Message(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
