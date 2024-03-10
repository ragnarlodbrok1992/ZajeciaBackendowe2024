from logging import getLogger

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from django.contrib.auth.models import Permission

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

# TODO: TemplateView renderuje template raz a potem nie reaguje na zmiany w bazie danych modeli - do poprawienia?

from django.urls import reverse_lazy, reverse

from viewer.models import Movie, Genre, Actor
from viewer.forms import MovieForm, ActorForm, SignUpForm


LOGGER = getLogger()
LOGGER.setLevel('INFO')


def viewer_403_handler(request, exception, template_name='403.html'):
    print("Exception:", exception)
    response = render(request, template_name)
    response.status_code = 403
    return response


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class MoviesAllView(ListView):
    template_name = 'movies.html'
    model = Movie
    # extra_context = {'movies': Movie.objects.all()}  # Pozostalosc po TemplateView


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


class MovieSelection(View):
    def get(self, request):

        movies = Movie.objects.all()

        return render(
            request, template_name='movie_selection.html',
            context={'movies': movies}
        )

    def post(self, request):
        button_url = request.POST.get('button')
        selected_movie = request.POST.get('movie_selection')  # Tutaj jest albo ID filmu albo None

        if button_url == 'create_movie':
            return redirect(reverse('movie_create'))
        elif not selected_movie:
            return redirect('index')
        elif button_url == 'update_movie':
            return redirect(reverse('movie_update', args=[selected_movie]))
        elif button_url == 'delete_movie':
            return redirect(reverse('movie_delete', args=[selected_movie]))
        else:
            return redirect('index')


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


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # template_name = 'form.html'
    template_name = 'model.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # template_name = 'form.html'
    template_name = 'model.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided incorrect data while updating movie.')
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin,
                      StaffRequiredMixin,
                      PermissionRequiredMixin,
                      DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'

    def post(self, request, *args, **kwargs):

        button_url = request.POST.get('button')

        # Wymaganie 1: W przypadku wciśnięcia przycisku - nie chce usuwać filmu -
        # wróc do strony głównej bez usuwania filmu
        # Klient zmienił zdanie - chce wrócić do wyboru filmu
        if button_url == "movie_select":  # Akcja wciśnięcia przycisku, która przyszła do nas
            # z frontu (my jesteśmy backendem)
            return redirect(reverse('movie_selection'))

        return super().post(request, *args, **kwargs)


class ActorCreateView(CreateView):
    template_name = 'form.html'
    form_class = ActorForm
    success_url = reverse_lazy('actors')


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

"""
ZADANIE 15:
    Miłego weekendu!
"""
