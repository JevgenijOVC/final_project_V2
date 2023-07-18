from django.db import models
from crm.models import Supplier, Customer


class Unit(models.Model):
    unit = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['unit']

    def __str__(self):
        return f'{self.unit}'


class ComponentType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# class OperationType(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#
#     class Meta:
#         ordering = ['name']
#
#     def __str__(self):
#         return f'{self.name}'


