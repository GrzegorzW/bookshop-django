from django.shortcuts import render

from models import Contact


def contact(request):
    context = {
        'contact': Contact.objects.filter(active=True).order_by('-id')[0]
    }
    return render(request, 'contact/contact.html', context)
