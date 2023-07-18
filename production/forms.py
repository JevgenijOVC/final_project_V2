from django.contrib import admin
from django import forms
from .models import Part, Component, Operation, OperationsForPart
from .admin import PartAdmin


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = [
            'part_drawing_code',
            'part_name',
            'part_drawings',
            'wood',
            'wood_type',
            'fsc_status',
            'quality_type',
        ]


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = [
            'name',
            'description',
            'type',
            'supplier',
            'price',
        ]


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = [
            'operation_name',
            'operation_description',
            'operation_cost_h',
        ]


class OperationsForPartForm(forms.ModelForm):
    class Meta:
        model = OperationsForPart
        fields = [
            'operation',
            'setup_time',
            'processing_time',
            'operation_comment',
        ]
