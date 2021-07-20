from django.contrib import admin
from .models import Product, Category, ReturnProduct

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'country',
        'price',
        'image',
        'in_stock',
    )

    exclude = ('id',)

    ordering = ('id',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'friendly_name',
            'name',
        )

class ReturnProductAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'return_reason',
    

        )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReturnProduct, ReturnProductAdmin)
