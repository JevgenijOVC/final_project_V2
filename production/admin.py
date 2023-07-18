from django.contrib import admin
from .models import OperationsForPart, Part, Component, Operation


class OperationInLine(admin.TabularInline):
    model = OperationsForPart
    fields = ()
    extra = 0


class PartAdmin(admin.ModelAdmin):
    inlines = [OperationInLine]

    class Meta:
        model = Part


admin.site.register(Part, PartAdmin)
admin.site.register(Component)
admin.site.register(Operation)
