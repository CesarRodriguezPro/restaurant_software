from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('list/', views.AppointmentListView.as_view(), name='list'),
    path('inactive/', views.AppointmentInactiveListView.as_view(), name='inactive'),
    path('create/', views.AppointmentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.AppointmentDetailView.as_view(), name='detail'),
]