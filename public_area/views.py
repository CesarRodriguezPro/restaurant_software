from django.contrib.messages import success
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from appointments.forms import AppointmentOutSideForm
from company.models import Company


class Home(TemplateView):
    template_name = 'public_area/main.html'


class ExternalLink(View):
    def get(self, request,pk):
        company = get_object_or_404(Company, pk=pk)
        form = AppointmentOutSideForm(pk=company.pk)
        return render(request, 'public_area/external.html', {'form': form})

    def post(self, request,pk):
        company = get_object_or_404(Company, pk=pk)
        form = AppointmentOutSideForm(request.POST, pk=company.pk)
        if form.is_valid():
            form_ = form.save(commit=False)
            form_.company = company
            form_.save()
            success(request, 'Appointment created successfully')
            return render(request, 'public_area/success.html', {'object': form.instance})
        return render(request, 'public_area/external.html', {'form': form})





