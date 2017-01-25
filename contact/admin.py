from django.contrib import admin

from .models import Contact, Message


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
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


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content',
        'created_at'
    )
