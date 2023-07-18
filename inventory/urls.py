from django.urls import path
from inventory import views


app_name = 'inventory'


urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/update/<int:pk>/', views.update_product, name='update_product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),

]
