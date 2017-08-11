from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^inscription$', views.inscription, name = 'new_inscription'),
	url(r'^connexion$', views.UserFormView.as_view(), name = 'connexion'),
	url(r'^find$', views.listeTransporteurs, name = 'transporteur'),

	
]

