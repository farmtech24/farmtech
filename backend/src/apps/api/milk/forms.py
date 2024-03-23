
from django import forms
from .models import DailyProduction

class DailyProductionForm(forms.ModelForm):
    """
    Form for adding daily milk production records.
    """
    class Meta:
        model = DailyProduction
        fields = ['date', 'milk_production', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
