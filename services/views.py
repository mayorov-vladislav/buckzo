from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Header, ServiceInfo, Client


class ServicesPage(TemplateView):
    template_name = 'services_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = Header.objects.all()
        services_info = ServiceInfo.objects.filter(is_visible=True)
        clients = Client.objects.filter(is_visible=True)
        context['headers'] = headers
        context['services_info'] = services_info
        context['clients'] = clients
        return context