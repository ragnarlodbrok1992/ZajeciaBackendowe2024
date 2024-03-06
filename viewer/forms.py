import re
from datetime import date
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm

from django.forms import (
    ModelForm, CharField,
    IntegerField, DateField,
)

from viewer.models import Movie, Actor


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized.")


def age_validator(value):
    age = (date.today() - value).days / 365
    print("Age:", age)
    if age < 16:
        raise ValidationError("Actor must be at least 16 years old.")


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Only past dates allowed here.")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=result.day)


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

    name = CharField(max_length=64, validators=[capitalized_validator])
    surname = CharField(max_length=64, validators=[capitalized_validator])
    birth_date = DateField(validators=[age_validator])


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    release_date = PastMonthField()

    def clean(self):
        cleaned_data = super().clean()

        # description = cleaned_data['description']

        # print("Description in clean method in MovieForm class", description)

        return cleaned_data

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split()

        print("Description in clean_description method in MovieForm class -->", initial)

        result = '. '.join(sentence.capitalize() for sentence in sentences)

        print("Description after changes in clean_description method in MovieForm class -->", result)

        return result


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        # self.instance.is_active = False  # Czy uzytkownik jest aktywny po zarejestrowaniu?
        return super().save(commit)
