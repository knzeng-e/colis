from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import SendingForm

# Create your views here.
def search_travel(request):
	form = SendingForm(request.POST or None)
	  
	if form.is_valid(): 
		pays_depart = form.cleaned_data['pays_depart'];
		pays_arrivee = form.cleaned_data['pays_arrivee']
		date_depart = form.cleaned_data['date_depart']
		contenu = form.cleaned_data['descriptif_colis']

	return render(request, 'search_travel.html', locals())

class TravelCreate(CreateView):
	model = Voyage
	fields = ['lieu_depart', 'lieu_arrivee', 'date_depart', 'date_arrivee', 'capacite', 'dispo_recup']
