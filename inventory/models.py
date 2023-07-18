from django.db import models
import random
from crm.models import Customer
from production.models import Component, Operation, Part
from utility.models import Unit


class Product(models.Model):
    code_id = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    product_drw_number = models.CharField(max_length=35, unique=True, null=True)
    product_drawings_1 = models.FileField(upload_to='production/drawings/', blank=True, null=True)
    product_drawings_2 = models.FileField(upload_to='production/drawings/', blank=True, null=True)
    product_drawings_3 = models.FileField(upload_to='production/drawings/', blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code_id:
            self.code_id = 'P' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['product_drw_number']

    def __str__(self):
        return f'{self.product_drw_number}{self.product_name}'


class PartsForProduct(models.Model):
    part = models.ForeignKey(Part, on_delete=models.RESTRICT, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True, null=True)


class ComponentsForProduct(models.Model):
    component = models.ForeignKey(Component, on_delete=models.RESTRICT, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.RESTRICT, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True, null=True)


class OperationsForProduct(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.RESTRICT, blank=True, null=True)
    setup_time = models.IntegerField(default=30, blank=True, null=True)
    processing_time = models.IntegerField(default=1, blank=True, null=True)
    operation_comment = models.CharField(max_length=150, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True, null=True)
