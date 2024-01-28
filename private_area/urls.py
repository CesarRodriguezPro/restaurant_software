from django.urls import path
from .views import Home, confirm_appointment

app_name = 'private_area'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('appointment/confirmed/<pk>', confirm_appointment, name='appointment_confirmed'),
]