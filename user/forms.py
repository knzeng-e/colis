from django.contrib.auth.models import User
from django import forms
from . import models


class InscriptionForm(forms.ModelForm):

	class Meta:
		model = models.User
		fields = '__all__'

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		
