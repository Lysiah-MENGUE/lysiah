from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class contact_form(forms.Form):
    name = forms.CharField(label='Nom', max_length=255)
    email = forms.EmailField(label='Adresse mail',max_length=255)
    entreprise = forms.CharField(label='Entreprise',max_length=255)
    message= forms.CharField(label='message',required=False,widget=forms.Textarea(attrs={'cols': 10, 'rows': 3}))