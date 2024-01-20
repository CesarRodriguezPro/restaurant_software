from django import forms
from phonenumber_field.formfields import PhoneNumberField
from appointments.models import Appointment


class AppointmentForm(forms.ModelForm):
    phone = PhoneNumberField(region="US",  help_text="Enter your phone number in the format: +1 123 456 7890")

    class Meta:
        model = Appointment
        fields = [
            'name',
            'phone',
            'time',
            'date',
            'number_of_people',
            'email',
            'message',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class AppointmentUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(region="US", help_text="Enter your phone number in the format: +1 123 456 7890")

    class Meta:
        model = Appointment
        fields = [
            "is_active",
            'name',
            'phone',
            'time',
            'date',
            'number_of_people',
            'email',
            'message',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


