from django.contrib import admin

# Register your models here.

from gestionProductos.models import Product,Category

class ProductsAdmin(admin.ModelAdmin):
    list_display=('name','description')
    search_fields=('name','description')

admin.site.register(Product,ProductsAdmin)
admin.site.register(Category)

