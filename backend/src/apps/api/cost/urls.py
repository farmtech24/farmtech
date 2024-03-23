# backend/apps/cost_structure/urls.py

from django.urls import path
from .views import (
    MaintenanceExpenseListCreateAPIView,
    MaintenanceExpenseRetrieveUpdateDestroyAPIView,
    InvestmentListCreateAPIView,
    InvestmentRetrieveUpdateDestroyAPIView,
    SalaryPaymentListCreateAPIView,
    SalaryPaymentRetrieveUpdateDestroyAPIView,
    TaxListCreateAPIView,
    TaxRetrieveUpdateDestroyAPIView,
    LivestockProductListCreateAPIView,
    LivestockProductRetrieveUpdateDestroyAPIView,
    CostStructureItemListCreateAPIView,
    CostStructureItemRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('maintenance-expenses/', MaintenanceExpenseListCreateAPIView.as_view(), name='maintenance-expense-list-create'),
    path('maintenance-expenses/<int:pk>/', MaintenanceExpenseRetrieveUpdateDestroyAPIView.as_view(), name='maintenance-expense-detail'),

    path('investments/', InvestmentListCreateAPIView.as_view(), name='investment-list-create'),
    path('investments/<int:pk>/', InvestmentRetrieveUpdateDestroyAPIView.as_view(), name='investment-detail'),

    path('salary-payments/', SalaryPaymentListCreateAPIView.as_view(), name='salary-payment-list-create'),
    path('salary-payments/<int:pk>/', SalaryPaymentRetrieveUpdateDestroyAPIView.as_view(), name='salary-payment-detail'),

    path('taxes/', TaxListCreateAPIView.as_view(), name='tax-list-create'),
    path('taxes/<int:pk>/', TaxRetrieveUpdateDestroyAPIView.as_view(), name='tax-detail'),

    path('livestock-products/', LivestockProductListCreateAPIView.as_view(), name='livestock-product-list-create'),
    path('livestock-products/<int:pk>/', LivestockProductRetrieveUpdateDestroyAPIView.as_view(), name='livestock-product-detail'),

    path('cost-structure/', CostStructureItemListCreateAPIView.as_view(), name='cost-structure-item-list-create'),
    path('cost-structure/<int:pk>/', CostStructureItemRetrieveUpdateDestroyAPIView.as_view(), name='cost-structure-item-detail'),
]
