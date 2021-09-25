from django.contrib import admin
from avodhashopapp.models import shop, Cat, Product
# Register your models here.


admin.site.register(shop)


class Catadmin(admin.ModelAdmin):
    prepopulated_fields = ({'slug': ('name',)})
    list_display = ['name', 'slug']


admin.site.register(Cat, Catadmin)


class Prodadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'image', 'availability', 'description']
    list_editable = ['price', 'stock', 'availability','description']
    prepopulated_fields = ({'slug': ('name',)})


admin.site.register(Product, Prodadmin)




