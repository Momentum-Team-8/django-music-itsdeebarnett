from django.db import models
from django.utils import timezone

# Create your models here.


class Album (models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

