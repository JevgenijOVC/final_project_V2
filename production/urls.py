from django.urls import path
from production import views

app_name = 'production'


urlpatterns = [
    path('parts/', views.part_list, name='part_list'),
    path('parts/<int:pk>/', views.part_detail, name='part_detail'),
    path('parts/create/', views.create_part, name='create_part'),
    path('parts/update/<int:pk>/', views.update_part, name='update_part'),
    path('parts/delete/<int:pk>/', views.delete_part, name='delete_part'),
    path('components/', views.component_list, name='component_list'),
    path('components/<int:pk>/', views.component_detail, name='component_detail'),
    path('components/create/', views.create_component, name='create_component'),
    path('components/update/<int:pk>/', views.update_component, name='update_component'),
    path('components/delete/<int:pk>/', views.delete_component, name='delete_component'),
    path('operations/', views.operation_list, name='operation_list'),
    path('operations/<int:pk>/', views.operation_detail, name='operation_detail'),
    path('operations/create/', views.create_operation, name='create_operation'),
    path('operations/update/<int:pk>/', views.update_operation, name='update_operation'),
    path('operations/delete/<int:pk>/', views.delete_operation, name='delete_operation'),
]