from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from user.models import User
#from .forms import Inscription


def home(request):
	return render(request, 'home.html')

def proposer(request):
	return render(request, 'proposer_trajet.html')

def profiles(request):
	users = User.objects.all()
			# return HttpResponseRedirect('/Inscription_Ok')
		# else:
			# form = InscriptionFor()
	return render(request, 'test.html', {'users': users})

#def get_name(request):
#	if request.method == 'POST':
#		form = Inscription(request.POST)
#		if form.is_valid():
#			nom = form.cleaned_data['name']
#			prenom = form.cleaned_data['prenom']
#			mail = form.cleaned_data['mail']
#			descript = form.cleaned_data['about']
#			return HttpResponseRedirect('/Inscription_Ok')
#	else:
#		form = Inscription()
#
#	return render(request, 'inscription.html')
#
def inscription(request):
	return render(request, 'inscription.html')