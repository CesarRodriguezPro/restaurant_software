import uuid
from django.urls import reverse_lazy
from appointments.email_functions import send_email_confirmation_to_user
from appointments.forms import AppointmentForm, AppointmentUpdateForm
from appointments.models import Appointment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.filter(is_active=True, company=self.request.user.company)


class AppointmentInactiveListView(LoginRequiredMixin, ListView):
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.filter(is_active=False, company=self.request.user.company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inactive'] = True
        return context


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('appointments:list')

    def get_form_kwargs(self):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        confirmation_number = uuid.uuid4()
        form.instance.confirmation_number = confirmation_number
        appointment = form.save()
        if appointment.email:
            send_email_confirmation_to_user(self.request.user.company.email, appointment)
        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentUpdateForm
    success_url = reverse_lazy('private_area:home')


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')



