from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import InscriptionForm
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View

def inscription(request):
	form = InscriptionForm(request.POST or None)
	print "Lancement de l'inscription"
	return render(request, 'user/inscription.html', locals())

class UserFormView(View):
	form_class = UserForm
	template_name = 'user/connexion.html'

	# Affichage d'un formulaire vide pour recueillir les donnees du user
	def get(self, request):
		form = self.form_class(None)
		print "connexion"
		return render(request, self.template_name, {'form': form})

	# Extraction des donnees du user en vue de l'ajouter dans la base de donnees
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid(): # si tous les champs obligatoires du formulaires sont saisis, 
							# on va verifier les infos entrees PUIS les enregister dans la BD

			user = form.save(commit = False)

			#verification des infos
			user_name = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password) # on crypte le mot de passe
			# prenom = form.cleaned_data['prenom']
			user.save()

			#une fois que le user est enregistre dans le BD, on l'authentifie
			user = authenticate(username = user_name, password = password) 	# la fonction verifie que le couple
																			# "user_name" + "password" existe et est correct

			if user is not None:
				if user.is_active:
					login(request, user) # connexion effective du user
					return redirect('accueil')

		return render(request, self.template_name, {'form': form})

def listeTransporteurs(request):

	search = request.POST
	result = Voyage.objects.all()
	print "Ville de depart ==> " + search['lieu_depart'] + "\nVille d'arrivee ==> " + search['lieu_arrivee']
	depart = search['lieu_depart']
	arrivee = search['lieu_arrivee']
	travel_date = search['date']
	result = result.filter(lieu_depart = depart).filter(lieu_arrivee = arrivee).filter(date_depart = travel_date)
	# result = get_object_or_404(Voyage, lieu_depart = depart, lieu_arrivee = arrivee, date_depart = travel_date)
	print result

	return render(request, 'show_travels.html', locals())

