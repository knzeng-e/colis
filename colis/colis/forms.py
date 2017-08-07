from django.contrib.auth.models import User
from django import forms
from .models import *



class SendingForm(forms.ModelForm):
	pays_depart = forms.CharField(max_length = 100)
	pays_arrivee = forms.CharField(max_length = 100)
	date_depart = forms.DateField()
	descriptif_colis = forms.CharField(widget = forms.Textarea)

		class Meta:
			model = Voyage
			fields = ['pays_depart', 'pays_arrivee', 'date_depart', 'descriptif_colis']

#class UserForm(forms.ModelForm):
#	password = forms.CharField(widget=forms.PasswordInput)



#class Inscription(forms.Form):
#	name = forms.CharField(label = "Nom", max_length=100)
#	prenom = forms.CharField(label = "Prénom", max_length=100)
#	mail = forms.EmailField(label = "Mail")
#	about = forms.CharField(widget=forms.Textarea)
