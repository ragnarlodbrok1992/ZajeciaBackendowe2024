from django.http import HttpResponse
from django.shortcuts import render

""" ZADANIE Domowe
    1. Modyfikujac funkcje 'hello' utworz program ktory:
      a) Przywita sie z userem jezeli ten poda imie
         - W przypadku braku imienia odpowie nam "Podaj swoje imie"
     b) Przy podaniu wieku odpisze nam pytanie "Kiedy sie urodziles?" i "Masz X lat"
     c) ** DLA CHETNYCH ** przekaz przez path albo parametr date, utworz obiekt datetime i go wyswietl na ekranie.
"""

""" ZADANIE 1
  1. Witamy wszystkich, oprocz:
    a) Macieja Oliwy
    b) Tomasza Nowaka
    Tym panom dziekujemy!
"""

BAD_PEOPLE_LIST = [
    ('Maciej', 'Oliwa'),
    ('Tomasz', 'Nowak')
]


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def powitanie(request, imie, nazwisko):
    if imie == "Maciej" and nazwisko == "Oliwa":
        return HttpResponse(f"TEMU PANU DZIEKUJEMY!!")
    return HttpResponse(f"Witaj {imie} {nazwisko}!")


def strona_glowna(request):
    return HttpResponse("Hello, SDA!!!")
