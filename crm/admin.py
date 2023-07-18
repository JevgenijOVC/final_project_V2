from django.contrib import admin
from .models import Customer, Supplier, SupplierMember, CustomerMember


admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(SupplierMember)
admin.site.register(CustomerMember)
