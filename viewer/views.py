from logging import getLogger

from django.shortcuts import render
from django.views import View
from django.views.generic import (
    TemplateView, ListView, CreateView
)

from django.urls import reverse_lazy

from viewer.models import Movie, Genre, Actor
from viewer.forms import MovieForm


LOGGER = getLogger()
LOGGER.setLevel('INFO')


class MoviesAllView(TemplateView):
    template_name = 'movies.html'
    model = Movie
    extra_context = {'movies': Movie.objects.all()}


class GenresAllView(ListView):
    template_name = 'generic.html'
    model = Genre


class ActorsAllView(ListView):
    template_name = 'actors.html'
    model = Actor


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


class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
