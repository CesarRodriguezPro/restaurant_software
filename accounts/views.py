from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import generic
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate


class LoginView(generic.View):
    def get(self, request):
        context = {
            'form': LoginForm(),
        }
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        post = request.POST
        email = post.get('email')
        password = post.get('password')

        print(email)
        print(password)

        user = authenticate(
            email=email,
            password=password,
        )
        if user:
            print('log in ')
            login(request, user)
            return redirect('private_area:home')
        messages.error(request, 'Wrong Email or Password')
        return redirect('accounts:login')


class RegisterView(generic.View):
    def get(self, request):
        return render(request, 'accounts/registration.html', context={'form': RegisterForm()})

    def post(self, request):
        post = request.POST
        form = RegisterForm(post)
        if form.is_valid():
            form_ = form.save(commit=False)
            form_.username = form.cleaned_data['email']
            form_.save()
            return redirect('accounts:registration_confirmation')
        messages.error(request, form.error_messages)
        return redirect('accounts:registration')


class RegistrationConfirmation(generic.TemplateView):
    template_name = 'accounts/registration_confirmation.html'
