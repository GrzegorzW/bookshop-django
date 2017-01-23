from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'about',
        'street',
        'city',
        'post_code',
        'phone',
        'logo',
        'smallLogo',
        'active'
    )
