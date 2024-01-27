from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import User
from company.models import Company
from restaurants.models import Restaurant


class Appointment(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Restaurant')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = PhoneNumberField()
    time = models.TimeField(verbose_name='time of reservation')
    date = models.DateField(verbose_name='Date of reservation')
    number_of_people = models.IntegerField(default=2, verbose_name='Number of guests')
    message = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    observer = models.BooleanField(default=False)
    observer_by = models.ManyToManyField(User, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time} - {self.restaurant}"
