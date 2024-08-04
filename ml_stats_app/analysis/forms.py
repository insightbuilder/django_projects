from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "dataset_instructions",
            "use_cases",
            "category",
        ]
        widgets = {
            "use_cases": forms.Textarea(attrs={"rows": 5}),
        }


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
