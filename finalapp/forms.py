from django import forms
from .models import Movie, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc', 'actor', 'year', 'category', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'desc']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
