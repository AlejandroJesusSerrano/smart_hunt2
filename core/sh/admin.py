from django.contrib import admin
from core.sh.models import *

# Equipos
admin.site.register(Brand)
admin.site.register(Dev_Type)
admin.site.register(Model)
admin.site.register(ImgPrinterDevice)
admin.site.register(Computer)
admin.site.register(Monitor)
admin.site.register(Peripherals)

# tecnicos
admin.site.register(Techs)

# Dependencias y oficinas
admin.site.register(Province)
admin.site.register(Location)
admin.site.register(Dependency)
admin.site.register(Edifice)
admin.site.register(Office)

# Empleados -usuarios de equipos-
admin.site.register(Employee)