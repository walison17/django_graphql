import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from django_graphql.core.models import Artist, Album, Song
from django_graphql.core.forms import ArtistForm


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class SongType(DjangoObjectType):
    artist = graphene.Field(ArtistType)

    class Meta:
        model = Song
        fields = ('name', 'size', 'number', 'album', 'artist')

    def resolve_artist(self, info):
        return self.album.artist


class Query:
    all_artists = graphene.List(ArtistType)
    all_songs = graphene.List(SongType)
    artist = graphene.Field(ArtistType, name=graphene.String())

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.prefetch_related('albums', 'albums__songs')

    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.select_related('album')

    def resolve_artist(self, info, name):
        return Artist.objects.get(name=name)


class CreateArtist(DjangoModelFormMutation):
    artist = graphene.Field(ArtistType)

    class Meta:
        form_class = ArtistForm


class Mutation:
    create_artist = CreateArtist.Field()
