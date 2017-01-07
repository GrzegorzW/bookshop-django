from __future__ import unicode_literals

from django.db import models
from djmoney.models.fields import MoneyField


class Shoe(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    size = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.brand + ' ' + self.name
