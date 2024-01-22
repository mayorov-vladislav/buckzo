from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Header, MainInfo, Work, WorkCategory, Footer


class IndexPage(TemplateView):
    template_name = 'main_buckzo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = Header.objects.all()
        main_infos = MainInfo.objects.filter(is_visible=True)
        works = Work.objects.filter(is_visible=True)
        work_categories = WorkCategory.objects.filter(is_visible=True)
        footers = Footer.objects.all()
        context['headers'] = headers
        context['main_infos'] = main_infos
        context['works'] = works
        context['work_categories'] = work_categories
        context['footers'] = footers
        return context

