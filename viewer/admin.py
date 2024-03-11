from django.contrib.admin import ModelAdmin
from datetime import datetime

# Register your models here.


class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.release_date.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):

        print("Request w cleanup_description:", request)
        print("Queryset w cleanup_description", queryset)

        for movie in queryset:
            print("Movie:", movie)
            obecne_description = movie.description
            if obecne_description:
                obecne_description += " DODATEK DO OPISU"
            else:
                obecne_description = "DODATEK DO OPISU"
            movie.description = obecne_description
            movie.save()

        # queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']

    readonly_fields = ['created_entry']

    fieldsets = [
        (None, {'fields': ['title', 'created_entry']}),
        (
            'External Information',
            {
                'fields': ['genre', 'release_date'],
                'description': 'These fields are going to be filled'
                               ' with data parsed from external'
                               ' databases.'
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]


class ActorAdmin(ModelAdmin):

    @staticmethod
    def age_calc(obj):
        return datetime.now().year - obj.birth_date.year

    @staticmethod
    def grant_Oscar(modeladmin, request, queryset):

        print("Adding an Oscarin backend: ", request)

        for actor in queryset:
            obecne_nagrody = actor.awards
            if obecne_nagrody:
                obecne_nagrody += ' Oscar,'
            else:
                obecne_nagrody = 'Oscar, '
            actor.awards = obecne_nagrody
            actor.save()

        # queryset.update(awards='Oscar')

    ordering = ['id']
    list_display = ['id', 'name', 'surname', 'age_calc']
    list_display_links = ['id', 'name', 'surname']
    list_per_page = 10
    list_filter = ['surname']
    search_fields = ['surname']
    actions = ['grant_Oscar']

    # readonly_fields = ['created_entry']

    fieldsets = [
        (None, {'fields': ['name', 'surname', 'age']}),
        (
            'External Information',
            {
                'fields': ['birth_date', 'place_of_birth'],
                'description': 'Data from external db.'
            }
        ),
        (
            'User Information',
            {
                'fields': ['awards'],
                'description': 'Data added by users.'
            }
        )
    ]
