from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from company.forms import CompanyCreateForm, CompanyUpdateForm
from company.models import Company


class CompanyList(LoginRequiredMixin, ListView):
    model = Company

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        return queryset


class CompanyInactiveList(LoginRequiredMixin, ListView):
    model = Company

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inactive'] = True
        return context


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company:list')


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    success_url = reverse_lazy('company:list')


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('company:list')

