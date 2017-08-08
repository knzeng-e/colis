from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import InscriptionForm

def inscription(request):
	form = InscriptionForm(request.POST or None)





	# if form.is_valid(): 
	# 	lieu_depart = form.cleaned_data['lieu_depart'];
	# 	lieu_arrivee = form.cleaned_data['lieu_arrivee']
	# 	date_depart = form.cleaned_data['date_depart']
	# 	contenu = form.cleaned_data['descriptif_colis']
	return render(request, 'user/inscription.html', locals())