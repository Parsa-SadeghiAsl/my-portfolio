from django import forms
from .models import Contact
from django.forms import ModelForm, TextInput, EmailInput, Textarea

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
           'message': Textarea(attrs={'class':'form-control', 'rows':5, 'cols':30})
        }
        