from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *
from .models import *


class AboutPage(TemplateView):
    template_name = 'about_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_headers = AboutUs.objects.all()
        clients = Client.objects.filter(is_visible=True)
        teams = Team.objects.filter(is_visible=True)
        about_infos = MainAboutInfo.objects.all()
        context['about_headers'] = about_headers
        context['clients'] = clients
        context['teams'] = teams
        context['about_infos'] = about_infos
        return context


# ---------------- API ----------------
class MainAboutApi(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutHeaderSerializer


class ClientApi(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TeamApi(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class MainAboutInfoApi(viewsets.ModelViewSet):
    queryset = MainAboutInfo.objects.all()
    serializer_class = MainAboutInfoSerializer


