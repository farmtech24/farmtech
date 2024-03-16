from rest_framework import serializers
from .models import Cow

class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cow
        fields = ['id', 'arete', 'nombre', 'nacimiento', 'numero_partos', 'lote', 'codigo_unico', 'category', 'additional_fields', 'photo']
