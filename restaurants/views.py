from django.shortcuts import render
from django.urls import reverse_lazy

from appointments.models import Appointment
from restaurants.models import Restaurant
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return Restaurant.objects.filter(company=self.request.user.company)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = 'restaurants/restaurant_detail.html'
    context_object_name = 'restaurant'


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'address', 'telephone', 'email']
    success_url = reverse_lazy('restaurants:restaurant_list')

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ['name', 'address', 'telephone', 'email']

    def get_queryset(self):
        return Restaurant.objects.filter(company=self.request.user.company)


class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurants/restaurant_delete.html'
    success_url = reverse_lazy('restaurant-list')

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


# htmx

def restaurant_appointments_active(request):
    restaurants = Appointment.objects.filter(
        company=request.user.company,
        is_active=True,
    ).order_by('date', 'time')
    context = {'object_list': restaurants, 'inactive': False}
    return render(request, 'restaurants/partials/appointments_table.html', context)


def restaurant_appointments_inactive(request):
    restaurants = Appointment.objects.filter(
        company=request.user.company,
        is_active=False,
    ).order_by('date', 'time')
    context = {'object_list': restaurants, 'inactive': True}
    return render(request, 'restaurants/partials/appointments_table.html', context)