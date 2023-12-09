from django.contrib import admin
from home.models import Contact,Patient,Doctor,medicine,patAmbulance,regAmbulances,ambulances
# Register your models here.
admin.site.register(Contact)  
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(medicine)
admin.site.register(patAmbulance)
admin.site.register(ambulances)
admin.site.register(regAmbulances)
