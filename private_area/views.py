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


def get_restaurant_appointments(request, pk):
    ### TODO: working on this
    print("get_restaurant_appointments")
    appointments = Appointment.objects.filter(
        date=datetime.datetime.now().date(),
        company=request.user.company,
        restaurant__pk=pk,
    ).order_by('time')

    print(appointments)
    context = {
        'objects_list': appointments,
        "restaurants": request.user.company.restaurants.all(),
    }
    return render(request, 'private_area/main.html', context)


def confirm_appointment(request, pk):
    if request.htmx:
        appointment = Appointment.objects.get(pk=pk)
        appointment.confirmed = True
        appointment.save()
        context = {'i': appointment}
        return render(request, 'private_area/partials/column.html', context)