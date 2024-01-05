from django.urls import path
from .views import Home

app_name = 'private_area'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]