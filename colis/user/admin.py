from django.contrib import admin
from models import *


class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'nom', 'prenom', 'date_de_naissance')
	ordering = ('id', )


class ColisAdmin(admin.ModelAdmin):
	list_display = ('id','poids', 'volume', 'contenu')

class EnvoiAdmin(admin.ModelAdmin):
	list_display = ('id', 'sender', 'colis')

class TransporteAdmin(admin.ModelAdmin):
	list_display = ('id_profil', 'colis')

class VoyageAdmin(admin.ModelAdmin):
	list_display = ('id_profil', 'lieu_depart', 'date_depart', 'lieu_arrivee', 'date_arrivee')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Colis, ColisAdmin)
admin.site.register(Envoi, EnvoiAdmin)
admin.site.register(Transporte, TransporteAdmin)
admin.site.register(Voyage, VoyageAdmin)
