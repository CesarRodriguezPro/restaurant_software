from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserPrivateAreaForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'date_joined',
            'last_login',
            'groups',
            'company',
            'is_manager',
            'is_owner',
            'user_permissions',
            'password',
        )


class CustomPasswordResetForm(forms.Form):

    password1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='New password confirmation', widget=forms.PasswordInput)

