from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import Movie


def movies_all(request):
    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )


def movies_by_genre(request, genre):
    # movies = Movie.objects.filter(genre__name=genre)

    # movies = Movie.objects.filter(genre__name__iexact=genre)

    movies = []
    for movie in Movie.objects.all():
        if movie.genre.name.lower() == genre.lower():
            movies.append(movie)

    return render(
        request, template_name='movies.html',
        context={'movies': movies}
    )


"""
ZADANIE 4  -> VIEW --> PATH(URL) --> CONTEXT --> TEMPLATE(SZABLON)
    a) Stworz nowy widok
    b) Przekaz parametr do funkcji (czyli poprzez path) <-- nazwa gatunku
    c) Przekaz przez context do widoku 'movies.html' dane na temat filmow danego gatunku
    d) Wyswietl te filmy w formie listy
"""


def powitanie(request, imie, nazwisko):
    if imie == "Maciej" and nazwisko == "Oliwa":
        return HttpResponse(f"TEMU PANU DZIEKUJEMY!!")
    return HttpResponse(f"Witaj {imie} {nazwisko}!")


def strona_glowna(request):
    return render(
        request, template_name='index.html',
        context={}
    )
