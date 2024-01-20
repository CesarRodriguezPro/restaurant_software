from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.CompanyList.as_view(), name='list'),
    path('inactive/', views.CompanyInactiveList.as_view(), name='inactive'),
    path('create/', views.CompanyCreate.as_view(), name='create'),
    path('update/<pk>/', views.CompanyUpdate.as_view(), name='update'),
    path('delete/<pk>/', views.CompanyDelete.as_view(), name='delete'),
    path('detail/<pk>/', views.CompanyDetail.as_view(), name='detail'),
]
