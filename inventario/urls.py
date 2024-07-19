# inventario/urls.py

from django.urls import path
from .views import material_list, material_create, material_update

urlpatterns = [
    path('', material_list, name='material_list'),
    path('create/', material_create, name='material_create'),
    path('update/<int:pk>/', material_update, name='material_update'),
]
