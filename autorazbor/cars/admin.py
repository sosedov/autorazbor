from django.contrib import admin

from .models import CarMark, CarModel, CarSubmodel


admin.site.register(CarMark)

admin.site.register(CarModel)

admin.site.register(CarSubmodel)