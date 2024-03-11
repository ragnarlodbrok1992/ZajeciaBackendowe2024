from django.contrib.admin import ModelAdmin

# Register your models here.


class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.release_date.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):

        print("Request w cleanup_description:", request)

        queryset.update(description=None)

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
