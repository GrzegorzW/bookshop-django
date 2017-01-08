from django.shortcuts import render

from books.models import Book
from genre.models import Genre


def books(request):
    genre_id = request.GET.get('genre')

    genre = Genre.objects.filter(id=genre_id)
    if genre:
        books = Book.objects.filter(genre=genre)
    else:
        books = Book.objects.all()

    genres = Genre.objects.filter(enabled=True)

    context = {
        'books': books,
        'genres': genres,
    }
    return render(request, 'store/books.html', context)


def book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'store/book.html', context)
