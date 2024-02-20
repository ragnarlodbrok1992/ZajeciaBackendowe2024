from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import Movie


def movies_all(request):
    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.all()}
    )


def powitanie(request, imie, nazwisko):
    if imie == "Maciej" and nazwisko == "Oliwa":
        return HttpResponse(f"TEMU PANU DZIEKUJEMY!!")
    return HttpResponse(f"Witaj {imie} {nazwisko}!")


def strona_glowna(request):
    return HttpResponse("Hello, SDA!!!")
