from django.contrib import admin
from .models import Order, ProductForOrder


class ProductInLine(admin.TabularInline):
    model = ProductForOrder
    fields = ()
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInLine]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductForOrder)
