from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'national_id',
            'marital_status',
            'name_spouse',
            'personal_email',
            'phone_number',
            'address',
            'city',
            'date_joining',
            'status',
            'salary',
            'department',
            'picture',
        ]

