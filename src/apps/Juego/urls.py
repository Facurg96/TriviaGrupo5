from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, registro, loginVista, logoutVista, HomeUsuario, resultado_pregunta, Jugar, tablero

urlpatterns = [

	path('', inicio, name='inicio'),
	path('login/', loginVista, name='login'),
	path('logout/', logoutVista, name='logout'),
	path('registro/', registro, name='registro'),
	path('Home/', HomeUsuario, name='home'),
	path('resultado/<int:pregunta_respondida_pk>/', resultado_pregunta, name='resultado_pregunta'),
	path('jugar/', Jugar, name='jugar'),
	path('tablero/', tablero, name='tablero'),

]