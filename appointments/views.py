from django.urls import reverse_lazy
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

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentUpdateForm
    success_url = reverse_lazy('appointments:list')


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')



