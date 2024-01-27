from django.urls import path
from . import views

app_name = 'restaurants'

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('create/', views.RestaurantCreateView.as_view(), name='restaurant_create'),
    path('detail/<pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('update/<pk>/', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('delete/<pk>/', views.RestaurantDeleteView.as_view(), name='restaurant_delete'),

    path('appointments_active/', views.restaurant_appointments_active, name='restaurant_appointments_active'),
    path('appointments_inactive/', views.restaurant_appointments_inactive, name='restaurant_appointments_inactive'),
]