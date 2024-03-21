from django.db import models
from urllib3.util import request


class Image(models.Model):
    user_id = models.IntegerField(blank=True)
    url_to_file = models.ImageField()
    coordinates = models.TextField(blank=True)
    metadata = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    user_id = models.IntegerField(blank=True)
    url_to_file = models.FileField()
    tags = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)


class Album(models.Model):
    is_private = models.BooleanField(default=True)
    participant_ids = models.TextField()
    image_ids = models.TextField(blank=True)
    video_ids = models.TextField(blank=True)

