from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField
from appointments.models import Appointment
from restaurants.models import Restaurant


class AppointmentForm(forms.ModelForm):
    phone = PhoneNumberField(
        region="US",  help_text="Enter your phone number in the format: +1 123 456 7890", required=False)

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['restaurant'].queryset = Restaurant.objects.filter(company=user.company)
            self.fields['restaurant'].initial = Restaurant.objects.filter(company=user.company).first()

    class Meta:
        model = Appointment
        fields = [
            'name',
            "restaurant",
            'phone',
            'time',
            'date',
            'number_of_people',
            'email',
            'message',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': timezone.now().date()}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'value': timezone.now().strftime("%H:%M")}),
        }


class AppointmentOutSideForm(forms.ModelForm):
    phone = PhoneNumberField(
        region="US",  help_text="Enter your phone number in the format: +1 123 456 7890", required=False)

    def __init__(self, *args, **kwargs):

        user = kwargs.pop('user', None)
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['restaurant'].queryset = Restaurant.objects.filter(company=user.company)
            self.fields['restaurant'].initial = Restaurant.objects.filter(company=user.company).first()

    class Meta:
        model = Appointment
        fields = [
            'name',
            "restaurant",
            'phone',
            'time',
            'date',
            'number_of_people',
            'email',
            'message',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': timezone.now().date()}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'value': timezone.now().strftime("%H:%M")}),
        }

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data.get("number_of_people")
        if number_of_people > 8:
            raise ValidationError("For groups larger than 8, please call for appointments.")
        return number_of_people

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if not phone and not email:
            raise ValidationError("Please provide either a phone number or an email address.")


class AppointmentUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(region="US", help_text="Enter your phone number in the format: +1 123 456 7890")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AppointmentUpdateForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['restaurant'].queryset = Restaurant.objects.filter(company=user.company)
            self.fields['restaurant'].initial = Restaurant.objects.filter(company=user.company).first()

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
            'confirmed',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data.get("number_of_people")
        if number_of_people > 8:
            raise ValidationError("For groups larger than 8, please call for appointments.")
        return number_of_people

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if not phone and not email:
            raise ValidationError("Please provide either a phone number or an email address.")

