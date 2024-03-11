from django.contrib.admin import ModelAdmin

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


"""
ZADANIE 16:

    Zmodyfikuj formularz oraz widok dla Aktora w panelu administratora:
    1) Stworz dwie grupy - User Information oraz External Information
    2) Uzupełnij pola dla tych dwóch grup.
    3) Age niech będzie readonly.
    4) Stworz funkcje, ktora przyznaje aktorom oskara!
    
    Widok listy aktora pozostawiam wam.
    Po czym sortowac? --> Sprobujcie daty urodzenia.

"""
