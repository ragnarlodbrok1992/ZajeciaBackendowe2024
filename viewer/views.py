from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from viewer.models import Movie


def movies_all(request):
    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.all()}
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


class StronaGlownaView(View):
    def get(self, request):
        return render(
            request, template_name='index.html',
            context={}
        )


class MoviesByGenreView(View):
    def get(self, request, genre):
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
