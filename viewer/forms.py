import re
from datetime import date
from django.core.exceptions import ValidationError

from django.forms import (
    Form, CharField, ModelChoiceField,
    IntegerField, DateField, Textarea
)

from viewer.models import Genre


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Only past dates allowed here.")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=result.day)


class MovieForm(Form):
    title = CharField(max_length=128, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    release_date = PastMonthField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split()

        return '. '.join(sentence.capitalize() for sentence in sentences)
