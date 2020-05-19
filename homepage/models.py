from __future__ import unicode_literals

from django.db import models

class Games(models.Model):
    titulo = models.CharField(max_length=255)
    plataformas = models.CharField(max_length=255)
