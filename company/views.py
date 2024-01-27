from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from company.models import Company


class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'

    def form_valid(self, form):
        user = self.request.user
        user.company = form.save()
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company:detail', kwargs={'pk': self.object.id})


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('company:detail', kwargs={'pk': self.object.id})


class CompanyDetail(LoginRequiredMixin, DetailView):
    model = Company


def go_to_company(request):

    print(request.user.company)
    if request.user.company:
        print('company exists')
        return redirect(reverse('company:detail', kwargs={'pk': request.user.company.id}))
    else:
        print('company does not exist')
        return redirect(reverse('company:create'))
