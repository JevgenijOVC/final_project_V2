from django.urls import path
from crm import views

app_name = 'crm'

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('suppliers/create/', views.create_supplier, name='create_supplier'),
    path('suppliers/update/<int:pk>/', views.update_supplier, name='update_supplier'),
    path('suppliers/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/update/<int:pk>/', views.update_customer, name='update_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),

]
