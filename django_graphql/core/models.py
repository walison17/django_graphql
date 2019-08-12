from django.db import models


class Artist(models.Model):
    name = models.CharField('Nome', max_length=50)
    genre = models.CharField('Gênero', max_length=50)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField('Título', max_length=50)
    release_year = models.IntegerField('Ano de lançamento')
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='albums'
    )

    class Meta:
        ordering = ('release_year', )

    def __str__(self):
        return self.title


class Song(models.Model):
    name = models.CharField('Nome', max_length=50)
    duration = models.TimeField('Duração')
    number = models.IntegerField('Número')
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name='songs'
    )

    class Meta:
        ordering = ['number']
        unique_together = ['album', 'number']

    def __str__(self):
        return self.name
