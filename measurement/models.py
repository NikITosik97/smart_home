from django.db import models
from django.db.models import CASCADE


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(unique=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=CASCADE, related_name='measurement')
    temperature = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
