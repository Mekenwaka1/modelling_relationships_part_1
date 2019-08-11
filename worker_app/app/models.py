from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=30)
    wage = models.CharField(max_length=30)

class Shift(models.Model):
    date = models.DateField()
    time = models.TimeField()

class Workers_shifts(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)