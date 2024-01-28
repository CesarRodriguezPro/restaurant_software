import datetime

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from appointments.models import Appointment


class Home(LoginRequiredMixin, View):
    def get(self, request):
        try:
            restaurants = request.user.company.restaurants.all()
            if restaurants.count() == 1:
                appointments = Appointment.objects.filter(
                    date=datetime.datetime.now().date(),
                    company=request.user.company,
                ).order_by('time')
            else:
                appointments = Appointment.objects.filter(
                    date=datetime.datetime.now().date(),
                    company=request.user.company,
                ).order_by('time')
            context = {
                'objects_list': appointments,
                "restaurants": restaurants,
            }
        except AttributeError:
            context = {
                'objects_list': [],
                "restaurants": [],
            }
        return render(request, 'private_area/main.html', context)


def confirm_appointment(request, pk):
    """
    htmx view to confirm an appointment
    when the user clicks on the button on the table
    in private_area/main.html template
    :param request:
    :param pk:
    :return:
    """
    if request.htmx:
        appointment = Appointment.objects.get(pk=pk)
        appointment.confirmed = True
        appointment.save()
        context = {'i': appointment}
        return render(request, 'private_area/partials/column.html', context)


