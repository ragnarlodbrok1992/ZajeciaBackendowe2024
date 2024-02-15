from django.http import HttpResponse

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


def hello(request):
    imie = request.GET.get('imie', 'WARTOŚĆ_DOMYŚLNA')
    nazwisko = request.GET.get('nazwisko', 'WARTOŚĆ_DOMYŚLNA')

    # if imie == "Maciej" and nazwisko == "Oliwa":
    #     return HttpResponse("Temu panu DZIEKUJEMY!!")
    # if imie == "Tomasz" and nazwisko == "Nowak":
    #     return HttpResponse("Temu panu DZIEKUJEMY!!")

    # for person in BAD_PEOPLE_LIST:
    #     if (imie, nazwisko) == person:
    #         return HttpResponse("TEGO PANA NIE OBSLUGUJEMY!!!!")

    if (imie, nazwisko) in BAD_PEOPLE_LIST:
        return HttpResponse("TEGO PANA NIE OBSLUGUJEMY!!!!")

    return HttpResponse(f"Hello, {imie} {nazwisko}!!!!")


def powitanie(request, imie, nazwisko):
    if imie == "Maciej" and nazwisko == "Oliwa":
        return HttpResponse(f"TEMU PANU DZIEKUJEMY!!")
    return HttpResponse(f"Witaj {imie} {nazwisko}!")


def strona_glowna(request):
    return HttpResponse("Hello, SDA!!!")
