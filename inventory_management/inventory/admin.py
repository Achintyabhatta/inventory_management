from django.contrib import admin

# Register your models here.
from .models import Customer, MedicalInformation

admin.site.register(Customer)
admin.site.register(MedicalInformation)
