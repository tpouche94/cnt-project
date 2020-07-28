
from django.db import models
from embed_video.fields import EmbedVideoField

class live(models.Model):
    video = EmbedVideoField()  # same like models.URLField()