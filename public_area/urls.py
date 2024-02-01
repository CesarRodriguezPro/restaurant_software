from django.urls import path
from . import views

app_name = 'public_area'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('external/<pk>/', views.ExternalLink.as_view(), name='external'),
    path('external/<pk>/success', views.ExternalLink.as_view(), name='success'),

]
