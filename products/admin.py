from django.contrib import admin
from .models import Product, Category, ReturnProduct, ProductFeedback

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
            'name',
            'id',
            'return_reason',   
        )


class ProductFeedbackAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'subject',
            'detail',   
        )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReturnProduct, ReturnProductAdmin)
admin.site.register(ProductFeedback, ProductFeedbackAdmin)
