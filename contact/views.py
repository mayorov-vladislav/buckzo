from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Header, Client, ContactUs
from .forms import ContactForm


class ContactPage(TemplateView):
    template_name = 'main_contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = Header.objects.all()
        clients = Client.objects.filter(is_visible=True)
        contacts_us = ContactUs.objects.all()
        context['headers'] = headers
        context['clients'] = clients
        context['contact_form'] = ContactForm()
        context['contacts_us'] = contacts_us
        return context

    def post(self, *args, **kwargs):
        contact_form = ContactForm(self.request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(self.request, 'Contact successfully')
            return redirect('/')

        context = self.get_context_data()
        context['contact_form'] = contact_form
        messages.error(self.request, 'Errors in Contact form')
        return render(self.request, self.template_name, context=context)
