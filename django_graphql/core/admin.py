from django.contrib import admin

from django_graphql.core.models import Artist, Album, Song


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre')
    inlines = [AlbumInline]


@admin.register(Song)
class SongModel(admin.ModelAdmin):
    list_display = ('number', 'name', 'duration')
