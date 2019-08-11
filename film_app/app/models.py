from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()

class Viewer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Film_viewers(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)