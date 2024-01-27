from django.urls import path
from .views import Home, get_restaurant_appointments, confirm_appointment

app_name = 'private_area'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('restaurant/<pk>/', get_restaurant_appointments, name='get_restaurant_active'),
    path('appointment/confirmed/<pk>', confirm_appointment, name='appointment_confirmed'),
]