from django.db.models import (
    Model, CharField, DO_NOTHING, DateField,
    DateTimeField, ForeignKey, IntegerField,
    TextField
)


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)  # TODO: dodac unikalnosc pola title dla wszystkich rekordow
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    release_date = DateField()
    description = TextField()
    created_entry = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


""" Zadanie 6 
a) Dodaj model Actor zawierajacy pola:
  - Imie
  - Nazwisko
  - Data urodzenia
  - Wiek
  - Nagrody
  - Miejsce urodzenia 
  
b) Stworz plik migracji (makemigration)
c) Przemigruj baze danych
d) Stworz widok ListView dla sciezki "actors/"
e) Stworz osobny szablon
f) Dodaj przycisk w pasku glownym aplikacji kierujacy do "actors/"
"""
