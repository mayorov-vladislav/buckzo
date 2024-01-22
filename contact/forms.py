from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='name',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Your Name',
                               'data-rule': 'minlen:4',
                               'data-msg': 'Please enter at least 4 chars',
                           }))
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Your Email',
                                 'class': 'form-control',
                                 'id': 'email',
                                 'data-rule': 'email',
                                 'data-msg': 'Please enter a valid email',
                             }))
    subject = forms.CharField(label='subject',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Subject',
                                  'data-rule': 'minlen:4',
                                  'data-msg': 'Please enter at least 4 chars'
                              }))
    message = forms.CharField(label='message',
                              widget=forms.Textarea(attrs={
                                  'placeholder': 'Message',
                                  'class': 'form-control',
                                  'rows': '5',
                              }))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']