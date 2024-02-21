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


class Actor(Model):
    name = CharField(max_length=64)
    surname = CharField(max_length=64)
    birth_date = DateField()
    age = IntegerField()
    awards = TextField()
    place_of_birth = CharField(max_length=128)

    def __str__(self):
        return f"{self.name} {self.surname}"


"""
Zadanie 7:
Stworz Formularz do tworzenia obiektow modelu Actor.

a) Stworz Form dla Actora (osobny plik forms.py).
b) Dodaj validator dla imienia i nazwiska.
c) Stworz odpowiedni widok.
d) Data urodzenia musi byc sprawdzona - aktor musi mieć co najmniej 16 lat.
e) Stworz template formularza do tworzenia obiektow aktorow. Pamietaj o csrf tokenie!
f) Pamietaj o dodaniu patha.

Przetestuj swoje rozwiazanie i dodaj paru aktorow.

"""
