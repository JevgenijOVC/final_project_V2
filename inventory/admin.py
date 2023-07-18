from django.contrib import admin
from inventory.models import Product, PartsForProduct, ComponentsForProduct, OperationsForProduct


class PartInLine(admin.TabularInline):
    model = PartsForProduct
    fields = ()
    extra = 0


class ComponentInLine(admin.TabularInline):
    model = ComponentsForProduct
    fields = ()
    extra = 0


class OperationInLine(admin.TabularInline):
    model = OperationsForProduct
    fields = ()
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PartInLine, ComponentInLine, OperationInLine]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(PartsForProduct)
admin.site.register(ComponentsForProduct)
admin.site.register(OperationsForProduct)

