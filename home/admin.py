from django.contrib import admin
from home.models import Contact,Patient,Doctor,medicine
# Register your models here.
admin.site.register(Contact)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(medicine)
