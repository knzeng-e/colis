from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

GENDER_CHOICES = (
   ('M', 'Masculin'),
   ('F', 'Feminin')
)

class User(models.Model):
	nom = models.CharField(max_length = 25, blank = False)
	prenom =models.CharField(max_length = 25, blank = False)
	user_name = models.CharField(max_length = 25)
	date_de_naissance = models.DateField()
	sexe = models.CharField(choices=GENDER_CHOICES, max_length=1)
	telephone = models.PositiveIntegerField()
	email = models.EmailField()
	photo = models.ImageField(upload_to = 'static/user/uploads/%Y/%m/%d/')
	
	def __str__(self):
		return "%s %s" % (self.nom, self.prenom)

class Colis(models.Model):
	poids = models.PositiveIntegerField()
	volume = models.PositiveIntegerField()
	contenu = models.TextField()
	def __str__(self):
		return (self.contenu)

class Envoi(models.Model):
	sender = models.ForeignKey('User')
	colis = models.ForeignKey('Colis')

	def __str__(self):
		return "Envoi de %s" %self.colis

class Transporte(models.Model):
	id_profil = models.ForeignKey('User')
	colis = models.ForeignKey('Colis')

class Voyage(models.Model):
	lieu_depart = models.CharField(max_length = 255)
	lieu_arrivee = models.CharField(max_length = 255)
	capacite = models.PositiveIntegerField()
	dispo_recup = models.SmallIntegerField()
	date_depart = models.DateField()
	date_arrivee = models.DateField()
	id_profil = models.ForeignKey('User')

	def __str__(self):
		return "%s %s -- %s -> %s" %(self.id_profil.prenom, self.id_profil.nom, self.lieu_depart, self.lieu_arrivee)
