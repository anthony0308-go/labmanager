# inventario/models.py
from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Utensil(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad  = models.IntegerField()

    def __str__(self):
        return self.nombre

class Equipment(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    materials = models.ManyToManyField(Material)
    utensils = models.ManyToManyField(Utensil)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"

