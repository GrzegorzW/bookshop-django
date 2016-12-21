from __future__ import unicode_literals
from djmoney.models.fields import MoneyField

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' ' + self.author
