# backend/apps/cost_structure/views.py

from rest_framework import generics
from .models import (
    MaintenanceExpense,
    Investment,
    SalaryPayment,
    Tax,
    LivestockProduct,
    CostStructureItem,
)
from .serializers import (
    MaintenanceExpenseSerializer,
    InvestmentSerializer,
    SalaryPaymentSerializer,
    TaxSerializer,
    LivestockProductSerializer,
    CostStructureItemSerializer,
)

class MaintenanceExpenseListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaintenanceExpense.objects.all()
    serializer_class = MaintenanceExpenseSerializer

class MaintenanceExpenseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceExpense.objects.all()
    serializer_class = MaintenanceExpenseSerializer

class InvestmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class SalaryPaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = SalaryPayment.objects.all()
    serializer_class = SalaryPaymentSerializer

class SalaryPaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalaryPayment.objects.all()
    serializer_class = SalaryPaymentSerializer

class TaxListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

class TaxRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

class LivestockProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = LivestockProduct.objects.all()
    serializer_class = LivestockProductSerializer

class LivestockProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LivestockProduct.objects.all()
    serializer_class = LivestockProductSerializer

class CostStructureItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = CostStructureItem.objects.all()
    serializer_class = CostStructureItemSerializer

class CostStructureItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostStructureItem.objects.all()
    serializer_class = CostStructureItemSerializer
