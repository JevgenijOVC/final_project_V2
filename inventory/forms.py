from django import forms
from .models import Product, PartsForProduct, ComponentsForProduct, OperationsForProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_drw_number',
            'product_drawings_1',
            'product_drawings_2',
            'product_drawings_3',
            'customer',
            'price'
        ]


class PartsForProductForm(forms.ModelForm):
    class Meta:
        model = PartsForProduct
        fields = [
            'part',
            'quantity',
            'unit',
        ]


class ComponentsForProductForm(forms.ModelForm):
    class Meta:
        model = ComponentsForProduct
        fields = [
            'component',
            'quantity',
            'unit',
        ]


class OperationsForProductForm(forms.ModelForm):
    class Meta:
        model = OperationsForProduct
        fields = [
            'operation',
            'setup_time',
            'processing_time',
            'operation_comment',
        ]
