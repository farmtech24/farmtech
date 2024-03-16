from django import forms
from .models import Cow

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['arete', 'nombre', 'nacimiento', 'numero_partos', 'lote', 'codigo_unico', 'category', 'additional_fields', 'photo']
