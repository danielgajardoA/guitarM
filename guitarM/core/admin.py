from django.contrib import admin
from .models import Mantencion, Tipo_Instrumento, Instrumento

# Register your models here.

class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','mantencion','tipo')
    search_fields = ('marca','modelo')

admin.site.register(Mantencion)
admin.site.register(Tipo_Instrumento)
admin.site.register(Instrumento, InstrumentoAdmin)
