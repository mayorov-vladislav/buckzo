from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import *
from .serializers import *


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


# ---------------API---------------
class HeaderApi(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class ServiceInfoApi(viewsets.ModelViewSet):
    queryset = ServiceInfo.objects.all()
    serializer_class = ServiceInfoSerializer


class ServicesClientApi(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

