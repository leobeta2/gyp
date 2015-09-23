from django.contrib import admin
from .models import Producto

class productoInline(admin.TabularInline):
    model = Producto
    extra = 3


class productoAdmin(admin.ModelAdmin):
  
    list_display = ('nombre', 'p_neto', 'p_web')
    #inlines = [productoInline]
    #list_filter = ['p_neto']
    search_fields = ['descripcion']

admin.site.register(Producto, productoAdmin)