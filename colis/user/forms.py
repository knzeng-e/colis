from django.contrib.auth.models import User
from django import forms


class SendingForm(forms.ModelForm):
	pays_depart = forms.CharField(max_length = 100)
	pays_arrivee = forms.CharField(max_length = 100)
	date_depart = forms.DateField()
	descriptif_colis = forms.CharField(widget = forms.Textarea)