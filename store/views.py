from django.shortcuts import render

from books.models import Book


def books(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'store/books.html', context)
