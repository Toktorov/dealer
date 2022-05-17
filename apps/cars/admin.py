from django.contrib import admin
from apps.cars.models import Brand, CarModel, Fuel, Transmission, DriveType, Car

# Register your models here.
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Fuel)
admin.site.register(Transmission)
admin.site.register(DriveType)
admin.site.register(Car)