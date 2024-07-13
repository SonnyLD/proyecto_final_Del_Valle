from django.contrib import admin # type: ignore

# Register your models here.

from .models import *

admin.site.register(Pasajero)
admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Pais_destino)