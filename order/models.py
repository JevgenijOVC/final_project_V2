from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import string
from crm.models import Customer
from inventory.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)


@receiver(pre_save, sender=Order)
def generate_component_code(sender, instance, **kwargs):
    if not instance.order_number:
        code = 'ORD-' + ''.join(random.choices(string.digits, k=5))
        instance.order_number = code

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return f'{self.order_number}'


class ProductForOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, blank=True, null=True)
