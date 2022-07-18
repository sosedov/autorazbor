from django.contrib import admin
from .models import Auto, Auto_Model, Auto_SubModel, Part, Part_Model
# Register your models here.
admin.site.register(Auto)
admin.site.register(Auto_Model)
admin.site.register(Auto_SubModel)
admin.site.register(Part)
admin.site.register(Part_Model)
