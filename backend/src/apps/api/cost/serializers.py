# backend/apps/cost_structure/serializers.py

from rest_framework import serializers
from .models import (
    MaintenanceExpense,
    Investment,
    SalaryPayment,
    Tax,
    LivestockProduct,
    CostStructureItem,
)

class MaintenanceExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceExpense
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']

class SalaryPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryPayment
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']

class LivestockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockProduct
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']

class CostStructureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostStructureItem
        fields = ['id', 'nombre', 'cantidad', 'precio', 'total']
