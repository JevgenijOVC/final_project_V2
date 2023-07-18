from django.contrib import admin
from django import forms
from .models import Order, ProductForOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'description',
            'customer'
        ]


class ProductForOrderForm(forms.ModelForm):
    class Meta:
        model = ProductForOrder
        fields = [
            'product',
            'quantity',
        ]
