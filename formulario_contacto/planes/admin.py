from django.contrib import admin

from planes.models import registro_cliente,nuevos_plan


class nuevoCliente(admin.ModelAdmin):
    list_display=("nombre","apellidoP","apellidoM","email","telefono")
    search_fields=("nombre","apellidoP","apellidoM","email","telefono")

class registro(admin.ModelAdmin):
        list_display=("nombre_plan","precio_plan","fecha_inicio","fecha_termino")
        search_fields=("nombre_plan")


admin.site.register(registro_cliente,nuevoCliente)
admin.site.register(nuevos_plan)



# Register your models here.