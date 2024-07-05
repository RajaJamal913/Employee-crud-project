# employees/forms.py
from django import forms # type: ignore
from .models import Employee_data

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_data
        fields = ['name', 'email', 'phone', 'salary']
