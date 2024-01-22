from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutHeader, Client, Team, MainAboutInfo


class AboutPage(TemplateView):
    template_name = 'about_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about_headers = AboutHeader.objects.all()
        clients = Client.objects.filter(is_visible=True)
        teams = Team.objects.filter(is_visible=True)
        about_infos = MainAboutInfo.objects.all()
        context['about_headers'] = about_headers
        context['clients'] = clients
        context['teams'] = teams
        context['about_infos'] = about_infos
        return context