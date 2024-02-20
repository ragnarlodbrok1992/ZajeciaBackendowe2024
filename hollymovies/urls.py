"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Movie
from viewer.views import movies_all, powitanie, strona_glowna

admin.site.register(Genre)
admin.site.register(Movie)

# Problem: zrzucanie danych z polskimi znakami do jsona powoduje error kodowania znaku
# Rozwiazanie: python -Xutf8 manage.py dumpdata viewer --output fixtures.json


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', strona_glowna),
    path('movies/', movies_all),
    path('powitanie/<imie>/<nazwisko>', powitanie),
]
