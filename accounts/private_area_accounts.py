from django.contrib.messages import success
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from accounts.forms import UserPrivateAreaForm, CustomPasswordResetForm
from accounts.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/private_area_accounts/user_list.html'

    def get_queryset(self):
        return User.objects.filter(is_active=True, company=self.request.user.company)


class UserInactiveListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/private_area_accounts/user_list.html'

    def get_queryset(self):
        return User.objects.filter(is_active=False, company=self.request.user.company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inactive'] = True
        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserPrivateAreaForm
    success_url = reverse_lazy('accounts:list')
    template_name = 'accounts/private_area_accounts/user_form.html'

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserPrivateAreaForm
    success_url = reverse_lazy('accounts:list')
    template_name = 'accounts/private_area_accounts/user_form.html'


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('accounts:list')
    template_name = 'accounts/private_area_accounts/user_confirm_delete.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    success_url = reverse_lazy('accounts:list')
    template_name = 'accounts/private_area_accounts/user_detail.html'


class ResetPassword(LoginRequiredMixin, View):

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        context = {'form': CustomPasswordResetForm(user)}
        return render(request, 'accounts/private_area_accounts/reset_password.html', context)

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        password_form = CustomPasswordResetForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            success(request, 'Your password was successfully updated!')
            return redirect('accounts:list')

