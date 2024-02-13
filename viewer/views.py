from django.http import HttpResponse

""" ZADANIE 
    1. Modyfikujac funkcje 'hello' utworz program ktory:
      a) Przywita sie z userem jezeli ten poda imie
         - W przypadku braku imienia odpowie nam "Podaj swoje imie"
     b) Przy podaniu wieku odpisze nam pytanie "Kiedy sie urodziles?" i "Masz X lat"
     c) ** DLA CHETNYCH ** przekaz przez path albo parametr date, utworz obiekt datetime i go wyswietl na ekranie.
"""


def hello(request):
    user = request.GET.get('user', 'UŻYTKOWNIK_DOMYŚLNY')
    wiek = request.GET.get('wiek', None)
    if wiek is None:
        return HttpResponse("ILE MASZ LAT?!?!?!")
    return HttpResponse(f"Hello, {user}, który ma {wiek} lat!!!")
