from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
        labels = {
            'email': '',
            'subject':'',
            'message':'',
         }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Your Email Adress'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Message Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder': 'Your Message Here'}),
         }
        