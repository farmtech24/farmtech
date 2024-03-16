from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.cow_list, name='cow_list'),
    path('upload/', views.upload_cow_photo, name='upload_cow_photo'),
    path('update/<int:cow_id>/', views.update_cow, name='update_cow'),
    path('delete/<int:cow_id>/', views.delete_cow, name='delete_cow'),
    path('add/', views.add_cow, name='add_cow'),
]
