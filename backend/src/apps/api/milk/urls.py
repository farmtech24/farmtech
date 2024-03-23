
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_daily_production, name='list_daily_production'),
    path('add/', views.add_daily_production, name='add_daily_production'),
    path('update/<int:pk>/', views.update_daily_production, name='update_daily_production'),
    path('delete/<int:pk>/', views.delete_daily_production, name='delete_daily_production'),
]
