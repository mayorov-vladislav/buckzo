from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *
from .models import *


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


# ---------------- API ----------------
class HeaderApi(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class MainInfoApi(viewsets.ModelViewSet):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer


class WorkCategoryApi(viewsets.ModelViewSet):
    queryset = WorkCategory.objects.all()
    serializer_class = WorkCategorySerializer


class WorkApi(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class FooterApi(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


