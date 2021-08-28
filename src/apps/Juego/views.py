from django.shortcuts import render, redirect
from .forms import RegistroForm, UsuarioLoginFormulario
from django.contrib.auth import authenticate, login, logout
from .models import UsuarioJuego



def inicio(request):

	ctx = {

		'bienvenido': 'Bienvenido'


	}


	return render(request, 'inicio.html', ctx)

def registro(request):

	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			#form = RegistroForm()
			return redirect('login')

	else:
		form = RegistroForm()

	context = {

		'form': form,
		#'titulo': titulo,

	}

	return render(request, 'Usuario/registro.html', context)

def loginVista(request):
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password= password)
		login(request, usuario)
		return redirect('home')

	context = {
		'form':form,
		'titulo':titulo

	}

	return render(request, 'Usuario/login.html', context)


def logoutVista(request):
	logout(request)
	return redirect('/')


def HomeUsuario(request):
	return render(request, 'Usuario/home.html')


def Jugar(request):
	UserJuego, created = UsuarioJuego.objects.get_or_create(usuario=request.user)
