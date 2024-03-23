from django.urls import path
from .views import *

urlpatterns = [
    path("album/<int:album_id>/", show_album, name='album'),
    path("upload_image/", upload_image, name='upload_image'),
    path("upload_video/", upload_video, name='upload_video'),
    path("profile/<int:profile_id>/", show_profile, name='show_profile'),
    path("login/", login_view, name='login'),
    path("register/", register, name='register'),
    path("logout", logout, name='logout'),
    path("profile_search/", profile_search, name='profile_search'),
]