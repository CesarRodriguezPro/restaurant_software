from django.contrib.messages import success
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from appointments.forms import AppointmentOutSideForm
from appointments.models import Appointment
from company.models import Company
from appointments.email_functions import send_email_confirmation_to_user
import uuid


class Home(TemplateView):
    template_name = 'public_area/main.html'


class ExternalLink(View):
    def get(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        form = AppointmentOutSideForm(pk=company.pk)
        return render(request, 'public_area/external.html', {'form': form})

    def post(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        form = AppointmentOutSideForm(request.POST, pk=company.pk)
        if form.is_valid():
            form_ = form.save(commit=False)
            confirmation_number = uuid.uuid4()
            form.instance.confirmation_number = confirmation_number
            form_.company = company
            form_.save()
            if form.instance.email:
                send_email_confirmation_to_user(company.email, form.instance)
            success(request, 'Appointment created successfully')
            return render(request, 'public_area/success.html', {'object': form.instance})
        return render(request, 'public_area/external.html', {'form': form})


class AppointmentLinkView(View):
    def get(self, request, uuid):
        appointment = Appointment.objects.get(confirmation_number=uuid)
        form = AppointmentOutSideForm(pk=appointment.company.pk, instance=appointment)
        return render(request, 'public_area/external.html', {'form': form})

    def post(self, request, uuid):
        appointment = Appointment.objects.get(confirmation_number=uuid)
        form = AppointmentOutSideForm(request.POST, pk=appointment.company.pk, instance=appointment)
        if form.is_valid():
            form_ = form.save(commit=False)
            form_.save()
            success(request, 'Appointment created successfully')
            return render(request, 'public_area/success.html', {'object': form.instance})
        return render(request, 'public_area/external.html', {'form': form})
