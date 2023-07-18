from django.db import models
from utility.constants.country_codes import COUNTRY_CHOICES


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['supplier_name']

    def __str__(self):
        return self.supplier_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ['customer_name']

    def __str__(self):
        return f'{self.customer_name}'


class SupplierMember(models.Model):
    supplier_company = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['supplier_company']

    def __str__(self):
        return f'{self.supplier_company}: {self.first_name} {self.last_name}'


class CustomerMember(models.Model):
    customer_company = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['customer_company']

    def __str__(self):
        return f'{self.customer_company}: {self.first_name} {self.last_name}'
