from django.urls import path
from .views import *

urlpatterns = [
    path("album/<int:album_id>/", show_album, name='album'),
    path("upload_image/", upload_image, name='upload_image'),
    path("upload_video/", upload_video, name='upload_video'),
    path("profile/", show_profile, name='show_profile'),
]