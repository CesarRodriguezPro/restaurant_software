from django.db import models
from accounts.models import User
from appointments.models import Appointment
from company.models import Company


class MessageSend(models.Model):
    send_by = models.ForeignKey(User, on_delete=models.CASCADE)
    send_date_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True,null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.appointment.name}"

