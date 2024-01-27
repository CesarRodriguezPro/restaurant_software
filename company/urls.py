from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('go_to_company/', views.go_to_company, name='go_to_company'),
    path('create/', views.CompanyCreate.as_view(), name='create'),
    path('update/<pk>/', views.CompanyUpdate.as_view(), name='update'),
    path('detail/<pk>/', views.CompanyDetail.as_view(), name='detail'),
]
