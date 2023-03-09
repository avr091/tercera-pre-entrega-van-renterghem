from django.db import models

# Create your models here.
class pistolas (models.Model):
    nombre=models.CharField(max_length=40)
    fps=models.IntegerField()

class aSalto (models.Model):
    nombre=models.CharField(max_length=30)
    fps=models.IntegerField()
    tipo=models.CharField(max_length=30)

class dMr (models.Model):
    nombre=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    fps=models.IntegerField()
   
