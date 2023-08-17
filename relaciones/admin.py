from django.contrib import admin
from .models import ModeloAuto,Fabricante,TipoCombustible,DirectorEjecutivo

# Register your models here.

# Otra forma de registar los models aquí, sería elaborando una lista para luego pasarla por el 'admin.site.register':
my_models = [ModeloAuto,Fabricante,TipoCombustible,DirectorEjecutivo]
admin.site.register(my_models)
# admin.site.register(Fabricante)
# admin.site.register(ModeloAuto)
# admin.site.register(TipoCombustible)
# admin.site.register(DirectorEjecutivo)


