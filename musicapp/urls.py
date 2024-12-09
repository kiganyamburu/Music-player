from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path("", views.index, name="index"),
    path("song/<int:song_id>/", views.detail, name="detail"),
    path("language/<str:language>/", views.language_songs, name="language_songs"),
    path("mymusic/", views.mymusic, name="mymusic"),
    path("playlist/", views.playlist, name="playlist"),
    path("playlist/<str:playlist_name>/", views.playlist_songs, name="playlist_songs"),
    path("favourite/", views.favourite, name="favourite"),
    path("all_songs/", views.all_songs, name="all_songs"),
    path("recent/", views.recent, name="recent"),
    path("play/<int:song_id>/", views.play_song, name="play_song"),
    path("play_song/<int:song_id>/", views.play_song_index, name="play_song_index"),
    path(
        "play_recent_song/<int:song_id>/",
        views.play_recent_song,
        name="play_recent_song",
    ),
]
