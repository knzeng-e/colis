from django.contrib.auth.models import User
from django import forms
from . import models


class InscriptionForm(forms.ModelForm):

	class Meta:
		model = models.User
		fields = '__all__'
		