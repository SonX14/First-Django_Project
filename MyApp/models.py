from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    icon = models.CharField(max_length=100, verbose_name='Icon', default='default.png')

