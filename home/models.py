from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField()
    email=models.TextField()
    designation=models.TextField()
    message=models.TextField()
   
class Patient(models.Model):
    name=models.TextField()
    age=models.TextField()
    email=models.TextField()
    sex=models.TextField()
    patId=models.TextField()
    history=models.TextField()

class PatID(models.Model):
    Patid=models.TextField()

class Doctor(models.Model):
    doctor=models.TextField()
    experience=models.TextField()
    Degree=models.TextField()
    Specialist=models.TextField()
    email=models.TextField()
class medicine(models.Model):
    name=models.TextField()
    patId=models.TextField()
    email=models.TextField()
    medicine=models.TextField()
    message=models.TextField()