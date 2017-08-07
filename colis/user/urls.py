from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.search_travel, name = 'search_travel'),
	url(r'Voyage/add/$', views.TravelCreate.as_view(), name = 'travel-add'),
]
