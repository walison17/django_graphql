from django import forms

from django_graphql.core.models import Artist


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', )
