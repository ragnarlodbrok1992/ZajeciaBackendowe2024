import datetime
import random

from viewer.models import Movie, Actor

import logging

req_logger = logging.getLogger('REQUEST_LOGGER')

STATIC_STRINGS = {'hello_message': "Witaj na stronie aplikacji Holly Movies!",
                  'date_created': "This site was created 3/04/2024"}
CIEKAWOSTKI = [
    "\"Back to the Future\": Director Robert Zemeckis originally wanted to cast Eric Stoltz as Marty McFly. "
    "Only after six weeks of filming did they decide on Michael J. Fox.",
    "\"Titanic\": Leonardo DiCaprio initially didn't want to star in James Cameron's film. "
    "He thought the story was too \"soft.\" Only after much persuasion from the director did "
    "he agree to the role of Jack Dawson.",
    "\"Star Wars\": Darth Vader was originally going to be played by David Prowse, but his strong English accent "
    "didn't fit the character. James Earl Jones provided the voice of Vader.",
    "\"Indiana Jones\": Harrison Ford wasn't the first choice for the role of Indiana Jones. "
    "George Lucas considered actors like Tom Selleck and Steve McQueen.",
    "\"Kill Bill\": Uma Thurman broke her hand in two places while filming the fight scene with Daryl Hannah. "
    "Despite this, she decided to finish the scene.",
]


def welcome_message(request):
    return STATIC_STRINGS


def autorzy(request):
    autors = ['Antoni Nieprzegoni',
              'Seweryn Kwaśniewski']
    return {'autors': autors}


def request_logger(request):
    raise NotImplementedError("Zaimplementuj logowanie requestow")


def ciekawostki(request):
    return {'ciekawostka': random.choice(CIEKAWOSTKI)}


def data_i_godzina(request):
    return {'current_time_and_date': datetime.datetime.now()}


def num_of_actors_and_movies(request):
    return {'num_of_actors': Actor.objects.count(),
            'num_of_movies': Movie.objects.count()}


"""
ZADANIE 11:

Dodaj następujące informacje do customowego context processora
i wyświetl informacje w osobnym widgetcie w base.html:
1. Ciekawostkę dnia na temat filmu/aktora (losuj z listy ciekawostek
   statycznie umiejscowionych w kodzie aplikacji).
2. Obecną datę i godzinę.
3. Informację na temat ilości aktorów/filmów w bazie danych.

1a* ---> Pobieraj ciekawostki z bazy danych też losowo.
      - MODEL
      - np jedno pole - cała ciekawostka
        ** - Odniesienie do filmów z bazy danych (jako foreign key)
    
      - Obiekty modeli można dodawać na pięć sposoby:
        - przez konsole
        - przez panel admina
        - przez użytkownika anonimowego
        - przez użytkownika zalogowanego
        - przez fixtures
        
      - (Do rozszerzenia) - to użytkownik może dodać ciekawostkę.

"""
