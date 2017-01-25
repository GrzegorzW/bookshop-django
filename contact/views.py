from django.shortcuts import render, redirect

from models import Contact
from .forms import MessageForm


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = MessageForm()

    context = {
        'contact': Contact.objects.filter(active=True).order_by('-id')[0],
        'form': form
    }
    return render(request, 'contact/contact.html', context)
