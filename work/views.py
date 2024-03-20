from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *
from .models import *


class WorksPage(TemplateView):
    template_name = 'work_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = Header.objects.all()
        works = Work.objects.filter(is_visible=True)
        work_categories = WorkCategory.objects.filter(is_visible=True)
        context['headers'] = headers
        context['works'] = works
        context['work_categories'] = work_categories
        return context


# --------------- API --------------
class HeaderWorkApi(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer


class WorkCategoryWorkApi(viewsets.ModelViewSet):
    queryset = WorkCategory.objects.all()
    serializer_class = WorkCategorySerializer


class WorkWorkApi(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

