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

class patAmbulance(models.Model):
    patId=models.TextField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.TextField()
    sex=models.TextField()
    area=models.TextField()
    city=models.TextField()

   
class ambulances(models.Model):
    driver_name=models.TextField()
    ambulance_number=models.TextField()
    number=models.TextField()
    area=models.TextField()
    city=models.TextField()
    status=models.TextField()

class regAmbulances(models.Model):
    pat_id=models.TextField()
    name=models.TextField()
    area=models.TextField()
    city=models.TextField()
    driver_name=models.TextField()
    phone_number=models.TextField()
    current=models.TextField()

class ImageDB(models.Model):
   photo=models.FileField(upload_to="media",max_length=250,null=True,default=None)