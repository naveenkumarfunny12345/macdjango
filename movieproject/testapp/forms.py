from django import forms
from django.core import validators 
from testapp.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

    def clean_hero(self):
        inputname=self.cleaned_data['hero']
        if len(inputname) < 4:
            raise forms.ValidationError('The Minimum no of characters in the name fieldshould be 4')
        return inputname
