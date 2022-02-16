from django.urls import path
from . import views 

urlpatterns = [
    # path("songs/", views.songs),
    # path("songs/<int:song_id>/", views.song_detail),
    path("posts/", views.posts),
    path("posts/<int:item_id>/", views.post_detail),
]