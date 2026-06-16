import uuid

from django.db import models

# Create your models here.


class Cam(models.Model):
    id_cam = models.CharField(max_length=100)
    external_id = models.CharField(max_length=100)

class Event_type(models.Model):
    event_type = models.CharField(max_length=100)

class Events(models.Model):
    type = models.CharField(max_length=50)
    event_type = models.ForeignKey(Event_type, on_delete=models.CASCADE)
    camera = models.ForeignKey(Cam, on_delete=models.CASCADE)
    image_uri = models.URLField(max_length=500)