from django.urls import path 
from .views import inicio, registro, loginVista, logoutVista, HomeUsuario, Jugar

urlpatterns = [

	path('', inicio, name='inicio'),
	path('login/', loginVista, name='login'),
	path('logout/', logoutVista, name='logout'),
	path('registro/', registro, name='registro'),
	path('Home/', HomeUsuario, name='home'),
	path('jugar/', Jugar, name='jugar'),

]