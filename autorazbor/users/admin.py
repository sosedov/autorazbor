from django.contrib import admin

from .models import User, Tariff


admin.site.register(User)

admin.site.register(Tariff)