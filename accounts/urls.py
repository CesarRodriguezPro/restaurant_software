from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import private_area_accounts as private_area

app_name = 'accounts'

urlpatterns = [
    path('login/',  views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('registration_confirmation/', views.RegistrationConfirmation.as_view(), name='registration_confirmation'),

    # Private area Users
    path('private_area/users/', private_area.UserListView.as_view(), name='list'),
    path('private_area/inactive_users/', private_area.UserInactiveListView.as_view(), name='list_inactive'),
    path('private_area/user/create/', private_area.UserCreateView.as_view(), name='create'),
    path('private_area/user/update/<int:pk>/', private_area.UserUpdateView.as_view(), name='update'),
    path('private_area/user/delete/<int:pk>/', private_area.UserDeleteView.as_view(), name='delete'),
    path('private_area/user/detail/<int:pk>/', private_area.UserDetailView.as_view(), name='detail'),
    path('reset-password/<pk>/', private_area.ResetPassword.as_view(), name='reset_password'),

]
