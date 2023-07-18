from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string

from crm.models import Supplier
from utility.constants.fsc_type import FSC_TYPE
from utility.constants.quality_type import QUALITY_TYPE
from utility.constants.wood import WOOD
from utility.constants.wood_type import WOOD_TYPE
from utility.models import ComponentType


# Create your models here.

class Component(models.Model):
    code_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    supplier = models.ManyToManyField(Supplier, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code_id:
            self.code_id = 'K' + str(random.randint(1, 9999))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['code_id']

    def __str__(self):
        return f'{self.code_id} - {self.name}'


class Part(models.Model):
    code_id = models.CharField(max_length=10, unique=True)
    part_drawing_code = models.CharField(max_length=255, blank=True, null=True, unique=True)
    part_name = models.CharField(max_length=255, blank=True, null=True)
    part_drawings = models.FileField(upload_to='production/drawings/', blank=True, null=True)
    wood = models.CharField(max_length=35, choices=WOOD, blank=True, null=True)
    wood_type = models.CharField(max_length=35, choices=WOOD_TYPE, blank=True, null=True)
    fsc_status = models.CharField(max_length=35, choices=FSC_TYPE, blank=True, null=True)
    quality_type = models.CharField(max_length=35, choices=QUALITY_TYPE, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code_id:
            self.code_id = 'G' + str(random.randint(1000, 9999))
        super(Part, self).save(*args, **kwargs)

    class Meta:
        ordering = ['code_id']

    def __str__(self):
        return f'{self.part_drawing_code} - {self.part_name}'


class Operation(models.Model):
    operation_name = models.CharField(max_length=7, blank=True, null=True)
    operation_description = models.CharField(max_length=255, blank=True, null=True)
    operation_cost_h = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['operation_name']

    def __str__(self):
        return f'{self.operation_name}'


class OperationsForPart(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.RESTRICT, blank=True, null=True)
    setup_time = models.IntegerField(default=30, blank=True, null=True)
    processing_time = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    operation_comment = models.CharField(max_length=150, blank=True, null=True)
    product = models.ForeignKey(Part, on_delete=models.RESTRICT, blank=True, null=True)
