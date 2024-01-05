from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserArea(LoginRequiredMixin, TemplateView):
    template_name = 'UserArea.html'


class Home(TemplateView):
    template_name = "index.html"
