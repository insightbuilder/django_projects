# employees/forms.py

from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "department",
            "position",
            "date_hired",
        ]


class BulkImportForm(forms.Form):
    csv_file = forms.FileField()
