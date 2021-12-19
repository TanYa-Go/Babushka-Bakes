from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
         }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Your Email'}),
            'subject': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Message Subject'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Your Message Here'}),
        }
