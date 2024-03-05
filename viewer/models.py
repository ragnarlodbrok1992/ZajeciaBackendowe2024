from django.db.models import (
    Model, CharField, DO_NOTHING, DateField,
    DateTimeField, ForeignKey, IntegerField,
    TextField
)

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


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


class Profile(AbstractBaseUser):
    username = CharField(max_length=32, unique=True)
    first_name = CharField(max_length=32)
    biography = TextField(blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
