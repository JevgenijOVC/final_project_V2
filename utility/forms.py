from django import forms
from .models import Unit, ComponentType


class UnitFrom(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class ComponentTypeFrom(forms.ModelForm):
    class Meta:
        model = ComponentType
        fields = '__all__'




