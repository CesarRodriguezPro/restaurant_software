from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'private_area/main.html'

