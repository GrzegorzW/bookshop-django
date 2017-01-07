from django.contrib import admin

from .models import Shoe


@admin.register(Shoe)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'description', 'size', 'price', 'price_currency', 'stock', 'created_at')
