from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    @classmethod
    def get_language_choices(cls):
        return [(language.code, language.name) for language in cls.objects.all()]


class Song(models.Model):

    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_img = models.FileField()
    song_file = models.FileField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    is_fav = models.BooleanField(default=False)


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
