from django.shortcuts import render

from books.models import Book
from genre.models import Genre


def books(request):
    genre_id = request.GET.get('genre')

    genre = Genre.objects.filter(id=genre_id)
    if genre:
        book_list = Book.objects.filter(genre=genre)
    else:
        book_list = Book.objects.all()

    context = {
        'books': book_list,
        'genres': Genre.objects.all,
    }
    return render(request, 'store/books.html', context)
