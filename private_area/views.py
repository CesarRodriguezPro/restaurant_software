import datetime

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from appointments.models import Appointment


class Home(LoginRequiredMixin, View):
    def get(self, request):
        appointments = Appointment.objects.filter(
            date__gte=datetime.datetime.now(),
            company=request.user.company,
        ).order_by('time')
        context = {'appointments': appointments}
        return render(request, 'private_area/main.html', context)

