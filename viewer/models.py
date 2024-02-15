from django.db.models import (
    Model, CharField, DO_NOTHING, DateField,
    DateTimeField, ForeignKey, IntegerField,
    TextField
)


class Genre(Model):
    name = CharField(max_length=128)


class Movie(Model):
    title = CharField(max_length=128)  # TODO: dodac unikalnosc pola title dla wszystkich rekordow
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    release_date = DateField()
    description = TextField()
    created_entry = DateTimeField(auto_now_add=True)
