from django.urls import path, include
from .views import under_construction, utility
from utility import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'utility'

urlpatterns = [
    path('under_construction/', under_construction, name='under_construction'),
    path('utility/', utility, name='utility'),
    path('units/', views.unit_list, name='unit_list'),
    path('units/create/', views.create_unit, name='create_unit'),
    path('units/update/<int:pk>/', views.update_unit, name='update_unit'),
    path('units/delete/<int:pk>/', views.delete_unit, name='delete_unit'),
    path('component_types/', views.component_type_list, name='component_type_list'),
    path('component_types/create/', views.create_component_type, name='create_component_type'),
    path('component_types/update/<int:pk>/', views.update_component_type, name='update_component_type'),
    path('component_types/delete/<int:pk>/', views.delete_component_type, name='delete_component_type'),
]

